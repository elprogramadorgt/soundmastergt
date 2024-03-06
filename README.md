# SoundMasterGT

Esta es una aplicación dedicada a eliminar los espacios vacios de tu video.

Espero te sea de mucha utilidad :blush:

Si deseas contribuir al proyecto eres bienvenido.

## Instrucciones

1. Ejecutar el archivo get_silence.sh

```bash
./get_silence.sh data/realtest.mp4 -30 1
```

- Recibe 3 parametros:
  1. La ruta del video
  2. la cantidad de decibeles donde se considera silencio
  3. la cantidad de segundos mínima para indentificar que debe considerarse como silencio

2. Ejecutar el archivo main6.py

```bash
python3 main6.py data/realtest.mp4 data/silence.mp4 silence.txt
```

- Recibe 3 parametros:

  1. La ruta del video a utilizar.
  2. La ruta del archivo generado
  3. La ruta del archivo silence.txt genrado por el script anterior.

  Enjoy :blush:
