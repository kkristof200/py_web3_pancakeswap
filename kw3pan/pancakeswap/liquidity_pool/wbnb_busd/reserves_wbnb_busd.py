# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Pip
from kw3.constants import Constants

# Local
from ..core.reserves import Reserves

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------- class: ReservesWbnbBusd --------------------------------------------------- #

class ReservesWbnbBusd(Reserves):

    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def reserveWbnb(self) -> int:
        return self.reserve0

    @property
    def reserveBusd(self) -> int:
        return self.reserve1

    @property
    def wbnb_busd_rate(self) -> float:
        return self.token0_token1_rate

    @property
    def busd_wbnb_rate(self) -> float:
        return self.token1_token0_rate


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def wbnbPrice(self) -> float:
        '''BUSD for 1 BNB'''
        return self.token0Price(Constants.WBNB.DECIMALS, Constants.BUSD.DECIMALS)

    def busdPrice(self) -> float:
        '''BNB for 1 Busd'''
        return self.token1Price(Constants.WBNB.DECIMALS, Constants.BUSD.DECIMALS)


# -------------------------------------------------------------------------------------------------------------------------------- #