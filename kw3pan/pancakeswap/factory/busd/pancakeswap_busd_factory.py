# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from kw3 import Web3
from kw3.constants import Constants

# Local
from ..core import PancakeswapFactory

from ...liquidity_pool import PancakeswapBusdLiquidityPool

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------- class: PancakeswapBusdFactory ------------------------------------------------ #

class PancakeswapBusdFactory(PancakeswapFactory):

    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def getPairAddress(
        self,
        address: str,
    ) -> Optional[str]:
        return super().getPairAddress(Constants.BUSD.ADDRESS, address)

    def getPair(
        self,
        address: str,
    ) -> Optional[PancakeswapBusdLiquidityPool]:
        pair_address = self.getPairAddress(address)

        return PancakeswapBusdLiquidityPool(
            web3=self._web3,
            address=pair_address
        ) if pair_address else None


# -------------------------------------------------------------------------------------------------------------------------------- #