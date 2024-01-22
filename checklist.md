# Community plugin checklist

- [ ] Review the official documentation: [New plugin checklist](https://github.com/microsoft/PowerToys/blob/main/doc/devdocs/modules/launcher/new-plugin-checklist.md)
- [ ] Package the plugin in a zip file
- [ ] Distribute the plugin via Assets in GitHub Releases
- [ ] The plugin and setting folders should be consistent
- [ ] The default action keyword for the plugin should be unique
- [ ] The website should be the URL to the GitHub repo for the plugin source code
- [ ] The documentation should be helpful to new users

## Zip

Package the plugin in a `.zip` archive file and distribute it by uploading it to a GitHub Release.

Examples:

✔️ <https://github.com/CoreyHayward/PowerToys-Run-InputTyper/releases/tag/v0.2.0>

Naming convention:

- `<name>-<version>-<platform>.zip`

Platform: `x64` | `ARM64`

Examples:

✔️ `InputTyper-0.2.0-x64.zip`

❌ `InputTyper.zip`

The zip file should contain:

- A folder with the same name as the plugin `AssemblyName`
- An `Images` folder with dark and light icons
- Plugin `DLL` files
- A `plugin.json` file

Examples:

✔️ `InputTyper-0.2.0-x64.zip`

```
Community.PowerToys.Run.Plugin.InputTyper
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

## Folders

After installation, the plugin and settings folder names should be consistent.

These folders are located here:

- `%LocalAppData%\Microsoft\PowerToys\PowerToys Run\Plugins`
- `%LocalAppData%\Microsoft\PowerToys\PowerToys Run\Settings\Plugins`
  - A folder here is created automatically if you use `PluginJsonStorage<T>`
  - The folder is given the same name as the `AssemblyName` of the plugin

Therefore, use the `AssemblyName` as the folder name for the plugin.

Examples:

✔️ `Community.PowerToys.Run.Plugin.InputTyper`

- `%LocalAppData%\Microsoft\PowerToys\PowerToys Run\Plugins\Community.PowerToys.Run.Plugin.InputTyper`
  - The plugin folder with images, `DLL` files and `plugin.json`
- `%LocalAppData%\Microsoft\PowerToys\PowerToys Run\Settings\Plugins\Community.PowerToys.Run.Plugin.InputTyper`
  - The settings folder with `.json` configuration files

## Action keyword

The plugin should have a unique default action keyword.

Action keywords for the out of the box plugins:

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
