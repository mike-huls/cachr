import random
from typing import Any

from .i_eviction_policy import ICacheStrategy


class RandomEvictionPolicy(ICacheStrategy):
    def on_access(self, cache: "BaseCache", key: Any) -> Any:
        """ Do Nothing """
        pass

    def on_insert(self, cache: "BaseCache", key: Any) -> None:
        """ Before item is inserted; check if we need to evict one """
        if len(cache.cache) >= cache.capacity:
            self.evict(cache=cache)

    def evict(self, cache: "BaseCache") -> None:
        """Evict the least recently used item."""
        if cache.cache:
            random_key = random.choice(list(cache.cache.keys()))
            cache.cache.pop(random_key)
