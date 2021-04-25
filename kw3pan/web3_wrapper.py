# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional
import random

# Pip
from kw3 import Web3, Bep20, Web3Wrapper as CoreWeb3Wrapper

from .pancakeswap import *

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: Web3Wrapper ------------------------------------------------------ #

class Web3Wrapper(CoreWeb3Wrapper):

    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Factory

    def pancakeswap_factory(self) -> Bep20:
        return PancakeswapFactory(self.__web3)

    def pancakeswap_wbnb_factory(self) -> PancakeswapWbnbFactory:
        return PancakeswapWbnbFactory(self.__web3)

    def pancakeswap_busd_factory(self) -> PancakeswapBusdFactory:
        return PancakeswapBusdFactory(self.__web3)


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
        return self.pancakeswap_wbnb_factory().getPair(
            address=token_address
        )

    def pancakeswap_busd_liquidity_pool_for_token(
        self,
        token_address: str
    ) -> PancakeswapLiquidityPool:
        return self.pancakeswap_busd_factory().getPair(
            address=token_address
        )

    def pancakeswap_wbnb_busd_liquidity_pool(self) -> PancakeswapWbnbBusdLiquidityPool:
        return PancakeswapWbnbBusdLiquidityPool(self.__web3)


# -------------------------------------------------------------------------------------------------------------------------------- #