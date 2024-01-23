# Community plugin checklist

- [ ] Review the official documentation: [New plugin checklist](https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/new-plugin-checklist.md)
- [ ] Package the plugin in a zip archive file
- [ ] The plugin folder should have the same name as the plugin
- [ ] The default action keyword for the plugin should be unique
- [ ] The website should be the URL to the GitHub repo for the plugin source code
- [ ] The documentation should be helpful to new users
- [ ] Distribute the plugin as an Asset via GitHub Releases

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

The plugin folder should have the same name as the plugin, and should not contain spaces.

Examples:

✔️ `InputTyper`

❌ `Input Typer`

❌ `Community.PowerToys.Run.Plugin.InputTyper`

In other words, the plugin folder name should match:

1. The name, without spaces, in the `plugin.json` file:
   - `"Name": "InputTyper"`
2. The last part of the assembly name:
   - `Community.PowerToys.Run.Plugin.InputTyper`

Community plugins are located here:

- `%LocalAppData%\Microsoft\PowerToys\PowerToys Run\Plugins`

For reference, the official plugins are located here:

- `C:\Program Files\PowerToys\RunPlugins\`

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

- Installation
- Usage
- Configuration

## Release

Distribute the plugin by attaching the `.zip` archive file to a GitHub Release.

Examples:

✔️ <https://github.com/CoreyHayward/PowerToys-Run-InputTyper/releases/tag/v0.2.0>
