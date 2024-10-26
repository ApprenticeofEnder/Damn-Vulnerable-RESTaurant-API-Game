import httpx
import asyncio
from faker import Faker


async def main():
    gen = Faker()

    username = gen.user_name()
    first_name = gen.first_name()
    last_name = gen.last_name()
    password = "Password1!"
    async with httpx.AsyncClient(base_url="http://localhost:8080/") as client:
        register_res = await client.post(
            "/register",
            json={
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "phone_number": last_name,
                "password": password,
            },
        )
        register_res.raise_for_status()
        login_res = await client.post(
            "/token", data={"username": username, "password": password}
        )
        login_res.raise_for_status()
        access_token = login_res.json()["access_token"]
        update_res = await client.put(
            "/profile",
            headers={"Authorization": f"Bearer {access_token}"},
            json={
                "username": "hhm",
                "first_name": "Pwned",
                "last_name": "Pwned",
                "phone_number": "123-456-7890",
            },
        )
        update_res.raise_for_status()


if __name__ == "__main__":
    asyncio.run(main())
