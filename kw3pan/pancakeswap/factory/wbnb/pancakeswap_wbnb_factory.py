# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from kw3 import Web3
from kw3.constants import Constants

# Local
from ..core import PancakeswapFactory

from ...liquidity_pool import PancakeswapWbnbLiquidityPool

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------- class: PancakeswapWbnbFactory ------------------------------------------------ #

class PancakeswapWbnbFactory(PancakeswapFactory):

    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def getPairAddress(
        self,
        address: str,
    ) -> Optional[str]:
        return super().getPairAddress(Constants.WBNB.ADDRESS, address)

    def getPair(
        self,
        address: str,
    ) -> Optional[PancakeswapWbnbLiquidityPool]:
        pair_address = self.getPairAddress(address)

        return PancakeswapWbnbLiquidityPool(
            web3=self._web3,
            address=pair_address
        ) if pair_address else None


# -------------------------------------------------------------------------------------------------------------------------------- #