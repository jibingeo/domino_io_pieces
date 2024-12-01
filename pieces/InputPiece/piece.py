from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from time import sleep


class InputPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info(f"Sleeping for {input_data.search} seconds")
        message = f"Sleep piece executed successfully for {input_data.search} seconds"
        self.logger.info(message)

        # Return output
        return OutputModel(
            message=message,
        )
