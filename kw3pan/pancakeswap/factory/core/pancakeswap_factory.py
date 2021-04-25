# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from kw3 import WrappedContract, Web3
from kw3.constants import Constants as KW3Constants

# Local
from ._abi import pancakeswap_factory_abi

from ...liquidity_pool import PancakeswapLiquidityPool, PancakeswapBusdLiquidityPool, PancakeswapWbnbLiquidityPool
from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------- class: PancakeswapFactory -------------------------------------------------- #

class PancakeswapFactory(WrappedContract):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3
    ):
        super().__init__(
            web3=web3,
            address=Constants.ADDRESS_PANCAKESWAP_FACTORY,
            abi=pancakeswap_factory_abi
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Forwarders

    def liquidityPoolAddressesLength(self) -> int:
        return self.functions.allPairsLength().call()

    def liquidityPoolAddressAtIndex(
        self,
        index: int
    ) -> str:
        return self.functions.allPairs(index).call()

    def liquidityPoolAtIndex(
        self,
        index: int
    ) -> PancakeswapLiquidityPool:
        return PancakeswapBusdLiquidityPool(
            web3=self._web3,
            address=self.liquidityPoolAddressAtIndex(
                index=index
            )
        )


    # Custom

    def getPairAddress(
        self,
        address0: str,
        address1: str
    ) -> Optional[str]:
        return self.functions.getPair(
            Web3.toChecksumAddress(address0),
            Web3.toChecksumAddress(address1)
        ).call()

    def getPair(
        self,
        address0: str,
        address1: str
    ) -> Optional[PancakeswapLiquidityPool]:
        return self.__getPair(
            PancakeswapLiquidityPool,
            address0=address0,
            address1=address1
        )

    def getWbnbPair(
        self,
        token_address: str
    ) -> Optional[PancakeswapWbnbLiquidityPool]:
        return self.__getPair(
            PancakeswapWbnbLiquidityPool,
            address0=KW3Constants.WBNB.ADDRESS,
            address1=token_address
        )

    def getBusdPair(
        self,
        token_address: str
    ) -> Optional[PancakeswapBusdLiquidityPool]:
        return self.__getPair(
            PancakeswapBusdLiquidityPool,
            address0=KW3Constants.BUSD.ADDRESS,
            address1=token_address
        )


    # ---------------------------------------------------- Private methods --------------------------------------------------- #

    def __getPair(
        self,
        _type,
        address0: str,
        address1: str
    ) -> Optional[PancakeswapLiquidityPool]:
        pair_address = self.getPairAddress(address0, address1)

        return _type(
            self._web3,
            pair_address
        ) if pair_address else None


# -------------------------------------------------------------------------------------------------------------------------------- #