from src.base_model import BaseModel, db
from src.moving.schemas import MoveBookingBodySchema


class MoveBookingModel(BaseModel):
    __tablename__ = 'move_bookings'

    entity_id = db.Column(db.String(200), db.ForeignKey("entities.uuid"), nullable=False)
    move_category = db.Column(db.String(200), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    origin = db.Column(db.String(255), nullable=False)
    mov_date = db.Column(db.String(255), nullable=False)
    mov_reason = db.Column(db.Text(), nullable=False, server_default="Move reason")
    mov_size = db.Column(db.String(255), nullable=False)
    move_to_building_type = db.Column(db.String(255), nullable=False)
    move_from_building_type = db.Column(db.String(255), nullable=False)
    items_to_move = db.Column(db.Text(), nullable=False)
    is_packaging_required = db.Column(db.Boolean(), nullable=False)
    is_dismantling_required = db.Column(db.Boolean(), nullable=False)
    is_storage_required = db.Column(db.Boolean(), nullable=False)

    def __init__(self, move: MoveBookingBodySchema):
        self.move_category = move.move_category
        self.entity_id = move.entity.uuid
        self.destination = move.destination
        self.origin = move.origin
        self.mov_date = move.mov_date
        self.mov_reason = move.mov_reason
        self.mov_size = move.mov_size
        self.move_to_building_type = move.move_to_building_type
        self.move_from_building_type = move.move_from_building_type
        self.items_to_move = move.items_to_move
        self.is_packaging_required = move.is_packaging_required
        self.is_dismantling_required = move.is_dismantling_required
        self.is_storage_required = move.is_storage_required

    def __repr__(self):
        return f"<Move {self.entity_id} [Origin: {self.origin} - Destination: {self.destination}]>"
