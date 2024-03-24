import json
import pprint
import aiohttp
import asyncio
import requests
access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJvcmRlcjphbGwiLCJwYXltZW50OmFsbCJdLCJleHAiOjE3MTEyNzUzNTYsImF1dGhvcml0aWVzIjpbInNoYXJkLWlkOnJ1LTAxIiwiY2xpZW50LWNpdHk60J3QvtCy0L7RgdC40LHQuNGA0YHQuiwg0J3QvtCy0L7RgdC40LHQuNGA0YHQutCw0Y8g0L7QsdC70LDRgdGC0YwiLCJjb250cmFjdDrQmNCcLdCg0KQt0JPQm9CTLTIyIiwiYWNjb3VudC1sYW5nOnJ1cyIsImFwaS12ZXJzaW9uOjEuMSIsImFjY291bnQtdXVpZDplOTI1YmQwZi0wNWE2LTRjNTYtYjczNy00Yjk5YzE0ZjY2OWEiLCJjbGllbnQtaWQtZWM1OmVkNzVlY2Y0LTMwZWQtNDE1My1hZmU5LWViODBiYjUxMmYyMiIsImNvbnRyYWN0LWlkOmRlNDJjYjcxLTZjOGMtNGNmNS04MjIyLWNmYjY2MDQ0ZThkZiIsImNsaWVudC1pZC1lYzQ6MTQzNDgyMzEiLCJjb250cmFnZW50LXV1aWQ6ZWQ3NWVjZjQtMzBlZC00MTUzLWFmZTktZWI4MGJiNTEyZjIyIiwic29saWQtYWRkcmVzczpmYWxzZSIsImZ1bGwtbmFtZTrQotC10YHRgtC40YDQvtCy0LDQvdC40LUg0JjQvdGC0LXQs9GA0LDRhtC40Lgg0JjQnCJdLCJqdGkiOiJsQU1HaHFpRDVmcWktQnFrX2htSFpFazktWDQiLCJjbGllbnRfaWQiOiJFTXNjZDZyOUpuRmlRM2JMb3lqSlk2ZU03OEpySmNlSSJ9.BKcJr_RGbbc7_xvVTRNe3yyQQVFSq9hRRTkCqqc0157KX8pYnSI89H2hz25wgjoRc6Jsyqv02YWAtkvgHqcRe17MnYCui3mJJY8a4QNjeStSRrizUO0TnwXRsk3YUCEmBNn2jeFjSHuAkBnHOoyizUmpgEMbose5WXJqYGLpCl_slMLi0S-RDmnd0fgrrQqQdw2YwI-xHNfFTyw8zGczSaYrny5TZepSrG9nYgDPh8n-BUbV9fDrNH5qwNoHo1trEYthl5HZd0oQmKcSO97e0lDI933lvkDULlYeaGxMTX2iX1p-obzE216WntDtmoAEppuw9UK0cTYqgOmrhTPWHQ'
authorization = {"Authorization" : "Bearer {}".format(access_token),'Content-Type': 'application/json'}

async def get_city_id(city:str, headers:dict[str]):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(
            'https://api.cdek.ru/v2/location/cities/?country_codes=RU',
            headers=headers
        ) as response:
            for city_info in json.loads(await response.text()):
                if city in city_info.values():
                    return city_info
                


if __name__ == '__main__':
    print(asyncio.run(get_city_id('Белгород',headers = authorization)))
