import html
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from patoolib import create_archive, extract_archive

LOGGER = logging.getLogger(__name__)


def pack(src: Path, title: str, include_xml: bool = False) -> Optional[Path]:
    files = []
    for index, img_file in enumerate(_get_folder(src, ('.jpg',))):
        files.append(img_file.rename(src.joinpath(f"{title}-{index:03}{img_file.suffix}")))
    files.append(src.joinpath('ComicInfo.json'))
    if include_xml and src.joinpath('ComicInfo.xml').exists():
        files.append(src.joinpath('ComicInfo.xml'))
    zip_file = src.parent.joinpath(title + '.cbz')
    if zip_file.exists():
        LOGGER.error(f"{zip_file.name} already exists in {zip_file.parent.name}")
        return None
    LOGGER.debug(f"Started packing of `{zip_file}`")
    create_archive(str(zip_file), [str(x) for x in files], verbosity=-1, interactive=False)
    LOGGER.debug(f"Finished packing of `{zip_file}`")
    return zip_file


def unpack(src: Path, dest: Path) -> Optional[Path]:
    process_folder = dest.joinpath(src.stem)
    if process_folder.exists():
        LOGGER.error(f"{process_folder.name} already exists in {process_folder.parent.name}")
        return None
    process_folder.mkdir(parents=True)
    LOGGER.debug(f"Started unpacking of `{src}` to `{process_folder}`")
    extract_archive(str(src), outdir=str(process_folder), verbosity=-1, interactive=False)
    LOGGER.debug(f"Finished unpacking of `{src}` to `{process_folder}`")
    return process_folder


def get_files(file: str, filter: Tuple[str, ...] = ('.cbz', '.cbr')) -> Set[Path]:
    path_file = Path(file)
    if not path_file.exists():
        return set()
    if path_file.is_dir():
        return set(_get_folder(path_file, filter))
    return {path_file}


def del_folder(folder: Path):
    for child in folder.iterdir():
        if child.is_file():
            child.unlink(missing_ok=True)
        else:
            del_folder(child)
    folder.rmdir()


def _get_folder(folder: Path, filter: Tuple[str, ...]) -> List[Path]:
    files = []
    for file in folder.iterdir():
        if not file.is_file():
            files.extend(_get_folder(file, filter))
        elif file.name.endswith(filter):
            files.append(file)
    return files


def safe_list_get(data: List[Any], index: int) -> Optional[Any]:
    try:
        return data[index]
    except (IndexError, KeyError):
        return None


def safe_dict_get(data: Dict[str, Any], key: str) -> Optional[Any]:
    try:
        return data[key]
    except (IndexError, KeyError):
        return None


def remove_annoying_chars(value: str) -> str:
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    return ' '.join(html.unescape(tag_re.sub('', value)).split())