import asyncio

async def shell_exec(code):
    process = await asyncio.create_subprocess_shell(
        code, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT
    )

    stdout = (await process.communicate())[0].decode().strip()
    return stdout, process

async def cssworker_url(target_url: str):
    url = "https://htmlcsstoimage.com/demo_run"
    my_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    }

    data = {
        "url": target_url,
        # Sending a random CSS to make the API to generate a new screenshot.
        "css": f"random-tag: {uuid.uuid4()}",
        "render_when_ready": False,
        "viewport_width": 1280,
        "viewport_height": 720,
        "device_scale": 1,
    }

    try:
        resp = await http.post(url, headers=my_headers, json=data)
        return resp.json()
    except HTTPError:
        return None