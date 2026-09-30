from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize the mcp
mcp=FastMCP("weather")

NWS_API_BASE="https://api.weather.gov/"
USER_AGENT="weather-app/1.0"

async def nws_weather_request(url:str)->dict[str,Any] | None:
    '''Makes a request to NWS API with proper handling'''
    headers={
        "User-Agent":USER_AGENT,
        "Accept":"application/geo-json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response=await client.get(url,headers=headers,timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_alert(feature:dict)->str:
    '''Format an alert feature into readable string'''
    props=feature["properties"]
    return f"""
    {feature}
Event:{props.get('event','Unknown')}
Area:{props.get('areaDesc','Unknown')}
Severity:{props.get('severity','Unknown')}
Decription:{props.get('description','No description')}
Instructions:{props.get('instruction','No instructions')}"""

@mcp.tool()
async def get_weather(state:str)->str:
    """Get Weather alerts for a US state.
    Args:
    state: 2-letter state code"""

    url=f"{NWS_API_BASE}/alerts/active/area/{state}"
    data=await nws_weather_request(url)

    if not data or "features" in data:
        return f"{data} unable to fetch alerts"
    
    alerts=[format_alert(feature) for feature in data["features"]]
    return '\n--\n'.join(alerts)