from fastapi import APIRouter


router = APIRouter(prefix="/orders", tags=['orders'])


@router.get("/")
async def list_orders():
    return [
        'order1',
        'order2',
        'order3',
    ]


@router.get("/{order_id}/")
async def get_order_by_id(order_id: int):
    return {
        'order': {
            'id': order_id,
        }
    }