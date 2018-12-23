# ColourApp
Fast way to get apps.

## How Does ColourApp Work?

`*` - Optional

`_` - Required

1. `*`**Downloads** the ColourApp from a server
2. `_`**Unpacks** the ColourApp from zip into a folder
3. `*`**Validates** the ColourApp for errors
4. `_`**Copies** the ColourApp source to `apps/...`

## Modules

### download.py (Planned)

Downloads ColourApps from servers.

### unpack.py

Unpackes ColourApp to `./unpacker_result`.

### validate.py

Validates `app_data.json`. Validation of core script coming soon.

### copy.py

Copies validated ColourApp contents to `/apps/...`

### core.py

Runs all the modules automatically.

### gui.py (Planned)

Simple GUI for ColourApp.

### cli.py (Planned)

Simple CLI for ColourApp.
