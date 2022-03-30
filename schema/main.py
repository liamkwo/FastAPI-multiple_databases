import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from starlette.staticfiles import StaticFiles
from api.settings import _VERSION_


description = """
docs🚀
"""

tags_metadata = [
    {
        "name": "",
        "description": "",
        "externalDocs": {
            "description": "",
            "url": "",
        },
    },
]

app = FastAPI(
    version=_VERSION_,
    title="",
    description=description,
    contact={
        "name": "",
        "url": "",
        "email": "",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=PlainTextResponse)
async def root():
    show_version = f"""                                                                                 
v{_VERSION_}                                                                          
"""

    return show_version

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=7777, reload=True)
