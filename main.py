from fastapi import  FastAPI, Query
import uvicorn

app = FastAPI()


hotels = [
    {"id": 1, "title": "Sochi"},
    {"id": 2, "title": "Dubai"}
]


@app.get("/hotels")
def get_hotels(
        id: int | None = Query(None, description="Айдишник"),
        title: str | None = Query(None, description="Название отеля")
):
    return [hotel for hotel in hotels if hotel["title"] == title or hotel["id"] == id]



@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "OK"}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
