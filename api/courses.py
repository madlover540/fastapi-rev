import fastapi

router = fastapi.APIRouter()

@router.get("/courses")
async def read_courses():
    return {"courses": []}

@router.post("/courses")
async def create_course():
    return "created"

@router.get("/courses/{id}")
async def read_course():
    return {"courses": []}

@router.patch("/courses/{id}")
async def update_course():
    return "updated"

@router.delete("/courses/{id}")
async def delete_course():
    return "deleted"