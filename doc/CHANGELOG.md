# Changelog
All notable changes to this project will be documented in this file.
 - `Added` for new features.
 - `Changed` for changes in existing functionality.
 - `Deprecated` for soon-to-be removed features.
 - `Removed` for now removed features.
 - `Fixed` for any bug fixes.
 - `Security` in case of vulnerabilities.
<hr>
 

## Upcoming features
- <br>
<hr>

## 2024-10-06 - v0.0.5
### Added
- `cache_info` method; accessible on cache object. Also on decorator 
- `refresh` method; accessible on cache object. Also on decorator 
- `clear` method; accessible on cache object. Also on decorator
- Unit tests for TTL cache decorator
<hr>

## 2024-08-27 - v0.0.4
### Changed
- `size` method is now a property 
<hr>

## 2024-08-27 - v0.0.3
### Changed
- Renamed `i_cache_strategy.py` to `cach_strategy.py` 
- Added CacheStrategy to cachr.__init__ so we can `from cachr import CacheStrategy` 
<hr>


## 2024-08-26 - v0.0.2
### Added
- Extended README
### Changed
- Renamed `ICacheStrategy` to `CacheStrategy` 
### Fixed
- Rename base cache from `CacheBlueprint` to `Cache` with `DefaultEvictionPolicy`
<hr>

## 2024-08-26 - v0.0.1
### Initial release 
<hr>
