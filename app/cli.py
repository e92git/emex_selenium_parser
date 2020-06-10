import sys
import json

from typing import Optional

import click

from .extractor import Extractor


@click.command()
@click.option('--vin', default=None)
@click.option('--frame', default=None, help='Used only with --framenum option')
@click.option('--framenum', default=None, help='Used only with --frame option')
@click.option('--proxy', default=None, help='proxy')
def extract_info(
        vin: Optional[str],
        frame: Optional[str],
        framenum: Optional[str],
        proxy: Optional[str],
):
    if vin is None and frame is None:
        raise ValueError('You have to specify either --vin or --frame argument')

    if vin:
        if frame:
            raise ValueError('You have to specify either --vin or --frame argument, not both at the same time')

        if framenum:
            raise ValueError('You have to specify either --vin or --framenum argument, not both at the same time')

    if frame:
        if not framenum:
            raise ValueError('You have to specify both of --frame and --framenum arguments')

    extractor = Extractor(proxy)

    if vin:
        data = extractor.extract_by_vin(vin)

    else:
        data = extractor.extract_by_framenum(frame, framenum)

    sys.stdout.write(json.dumps(data))