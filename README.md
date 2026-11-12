# Planet Express

A dark Oaxaca theme inspired by Futurama and computer science.

![Planet Express](backgrounds/1-deep-space.webp)

```bash
oaxaca theme install https://github.com/santisbon/planet-express-theme
```

The wallpapers are drawn by `src/gen.py`; `src/render.sh` rebuilds them.

## Your own backgrounds

To add backgrounds that stay on your machine, put them in `~/.config/oaxaca/backgrounds/planet-express/`, then reapply the theme:

```bash
mkdir -p ~/.config/oaxaca/backgrounds/planet-express
cp <your-image-file> ~/.config/oaxaca/backgrounds/planet-express/
oaxaca theme set planet-express
```

`oaxaca theme bg next` cycles through them together with the theme's own backgrounds.
