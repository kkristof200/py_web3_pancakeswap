# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from kw3 import KWeb3 as Web3

from .factory import *
from .liquidity_pool import *

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: Web3Wrapper ------------------------------------------------------ #

class PancakeSwap:
    
    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Optional[Web3] = None
    ):
        self.__web3 = web3 or Web3()
        
        self.__factory = None
        self.__factory_wbnb = None
        self.__factory_busd = None

    # --------------------------------------------------- Public properties -------------------------------------------------- #

    # Factory

    @property
    def factory(self) -> PancakeswapFactory:
        self.__factory = self.__factory or PancakeswapFactory(self.__web3)

        return self.__factory

    @property
    def factory_wbnb(self) -> PancakeswapWbnbFactory:
        self.__factory_wbnb = self.__factory or PancakeswapWbnbFactory(self.__web3)

        return self.__factory_wbnb

    @property
    def factory_busd(self) -> PancakeswapBusdFactory:
        self.__factory_busd = self.__factory or PancakeswapBusdFactory(self.__web3)

        return self.__factory_busd


    # Liquidity pool

    def pancakeswap_liquidity_pool(
        self,
        address: str
    ) -> PancakeswapLiquidityPool:
        return PancakeswapLiquidityPool(self.__web3, address=address)

    def pancakeswap_wbnb_liquidity_pool(
        self,
        liquidity_pool_address: str
    ) -> PancakeswapWbnbLiquidityPool:
        return PancakeswapWbnbLiquidityPool(
            web3=self.__web3,
            address=liquidity_pool_address
        )

    def pancakeswap_busd_liquidity_pool(
        self,
        liquidity_pool_address: str
    ) -> PancakeswapBusdLiquidityPool:
        return PancakeswapBusdLiquidityPool(
            web3=self.__web3,
            address=liquidity_pool_address
        )

    def pancakeswap_wbnb_liquidity_pool_for_token(
        self,
        token_address: str
    ) -> PancakeswapLiquidityPool:
        return self.factory_wbnb.getPair(
            address=token_address
        )

    def pancakeswap_busd_liquidity_pool_for_token(
        self,
        token_address: str
    ) -> PancakeswapLiquidityPool:
        return self.factory_busd.getPair(
            address=token_address
        )

    def pancakeswap_wbnb_busd_liquidity_pool(self) -> PancakeswapWbnbBusdLiquidityPool:
        return PancakeswapWbnbBusdLiquidityPool(self.__web3)


# -------------------------------------------------------------------------------------------------------------------------------- #