from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# static 파일 (1개월 캐시)
class CacheStaticFiles(StaticFiles):
    async def get_response(self, path, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 200:
            response.headers["Cache-Control"] = "public, max-age=2592000"
        return response

app.mount("/static", CacheStaticFiles(directory="static"), name="static")


# HTML 캐시 미들웨어 (1일)
@app.middleware("http")
async def html_cache_middleware(request: Request, call_next):
    response: Response = await call_next(request)

    content_type = response.headers.get("content-type", "")
    
    # HTML 응답이면 1시간 캐시
    if "text/html" in content_type:
        response.headers["Cache-Control"] = "public, max-age=3600"

    return response