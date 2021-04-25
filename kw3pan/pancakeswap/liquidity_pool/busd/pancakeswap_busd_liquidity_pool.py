# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from kw3 import Web3, Bep20, Busd
from kw3.constants import Constants

# Local
from .reserves_busd import ReservesBusd

from ..core import PancakeswapLiquidityPool

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- class: PancakeswapBusdLiquidityPool --------------------------------------------- #

class PancakeswapBusdLiquidityPool(PancakeswapLiquidityPool):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3,
        address: str
    ):
        super().__init__(
            web3=web3,
            address=address
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Custom

    def tokenAddress(self) -> Optional[str]:
        return self.token().address

    def token(self) -> Optional[Bep20]:
        return self.quoteToken() if self._is_base_busd() else self.baseToken()

    def busdAddress(self) -> Optional[str]:
        return self.busd().address

    def busd(self) -> Optional[Busd]:
        return self.baseToken() if self._is_base_busd() else self.quoteToken()

    def priceTokenCumulativeLast(self) -> int:
        return self.quoteTokenPriceCumulativeLast() if self._is_base_busd() else self.baseTokenPriceCumulativeLast()

    def priceBusdCumulativeLast(self) -> int:
        return self.baseTokenPriceCumulativeLast() if self._is_base_busd() else self.quoteTokenPriceCumulativeLast()

    def tokenPrice(self) -> Optional[float]:
        '''BUSD for 1 Token'''
        return self.quoteTokenPrice() if self._is_base_busd() else self.baseTokenPrice()

    def busdPrice(self) -> Optional[float]:
        '''Token for 1 BUSD'''
        return self.baseTokenPrice() if self._is_base_busd() else self.quoteTokenPrice()

    def toToken(
        self,
        busdAmount: int
    ) -> Optional[float]:
        '''Token for "busdAmount" BUSD'''
        return (self.toQuoteToken if self._is_base_busd() else self.toBaseToken)(busdAmount)

    def toBusd(
        self,
        tokenAmount: int
    ) -> Optional[float]:
        '''BUSD for "tokenAmount" Token'''
        return (self.toBaseToken if self._is_base_busd() else self.toQuoteToken)(tokenAmount)


    def getReserves(self) -> Optional[ReservesBusd]:
        return self._getReserves(
            ReservesBusd,
            is_base_busd=self._is_base_busd()
        )

    def tokenHoldings(self) -> Optional[int]:
        reserves = self.getReserves()

        return reserves.reserveToken if reserves else None

    def busdHoldings(self) -> Optional[int]:
        reserves = self.getReserves()

        return reserves.reserveBusd if reserves else None


    # ---------------------------------------------------- Private methods --------------------------------------------------- #

    def _is_base_busd(self) -> bool:
        if not hasattr(self, '__is_base_busd'):
            self.__is_base_busd = self.token0().address == Constants.BUSD.ADDRESS

        return self.__is_base_busd


# -------------------------------------------------------------------------------------------------------------------------------- #