# Community plugin checklist

- [ ] Review the official documentation: [New plugin checklist](https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/new-plugin-checklist.md)
- [ ] Package the plugin in a zip archive file
- [ ] The plugin folder should have the same name as the plugin
- [ ] The default action keyword for the plugin should be unique
- [ ] The website should be the URL to the GitHub repo for the plugin source code
- [ ] The documentation should be helpful to new users
- [ ] Distribute the plugin as an Asset via GitHub Releases
- [ ] Validate the plugin with [`ptrun-lint`](https://github.com/hlaueriksson/Community.PowerToys.Run.Plugin.Lint)

## Zip

Package the plugin in a `.zip` archive file.

Naming convention:

- `<name>-<version>-<platform>.zip`

Platform: `x64` | `ARM64`

Examples:

✔️ `InputTyper-0.2.0-x64.zip`

❌ `InputTyper.zip`

The zip file should contain:

- A folder with the same name as the plugin
  - An `Images` folder
    - with dark and light `.png` icons
  - Plugin `.dll` files
  - A `plugin.json` file

Examples:

✔️ `InputTyper-0.2.0-x64.zip`:

```
InputTyper
├── Images
│   ├── InputTyper.light.png
│   └── InputTyper.dark.png
├── Community.PowerToys.Run.Plugin.InputTyper.dll
├── Community.PowerToys.Run.Plugin.InputTyper.deps.json
└── plugin.json
```

Unnecessary files in the zip:

- `PowerToys.Common.UI.dll`
- `PowerToys.ManagedCommon.dll`
- `PowerToys.Settings.UI.Lib.dll`
- `Wox.Infrastructure.dll`
- `Wox.Plugin.dll`

## Folder

The plugin folder should have the same name as the plugin.

The name should be in `PascalCase`, i.e. without spaces or punctuation and with capitalized words.

Examples:

✔️ `InputTyper`

❌ `Input Typer`

❌ `Community.PowerToys.Run.Plugin.InputTyper`

In other words, the plugin folder name should match:

1. The name in the `plugin.json` file:
   - `"Name": "InputTyper"`
2. The last part of the assembly name:
   - `Community.PowerToys.Run.Plugin.InputTyper`

Community plugins are located here:

- `%LocalAppData%\Microsoft\PowerToys\PowerToys Run\Plugins`

For reference, the official plugins are located in one of these places:

- `C:\Program Files\PowerToys\RunPlugins`
  - Machine wide installation of PowerToys
- `%LocalAppData%\PowerToys\RunPlugins`
  - Per user installation of PowerToys

## Action Keyword

The plugin should have a unique default action keyword.

Action keywords for the official plugins:

- [Direct activation commands](https://learn.microsoft.com/en-us/windows/powertoys/run#direct-activation-commands)

Examples:

✔️ `@@`

❌ `=`

❌ `#`

❌ `??`

## Website

The website in the `plugin.json` should be the URL to the GitHub repo for the plugin source code.

Examples:

✔️ `"Website": "https://github.com/CoreyHayward/PowerToys-Run-InputTyper",`

❌ `"Website": "https://github.com/CoreyHayward",`

## Documentation

Help new users with instructions for:

- Requirements
- Installation
- Usage
- Configuration

## Release

Distribute the plugin by attaching the `.zip` archive file to a GitHub Release.

Examples:

✔️ <https://github.com/CoreyHayward/PowerToys-Run-InputTyper/releases/tag/v0.2.0>

## Lint

Run [`ptrun-lint`](https://github.com/hlaueriksson/Community.PowerToys.Run.Plugin.Lint) on the plugin and review the reported issues.

The lint rules are codified from the guidelines in this checklist.
