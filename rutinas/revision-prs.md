# Revisión de PRs

Avisa a cada persona de las PRs a `main` que esperan su revisión, aunque también le llegue el correo de GitHub. Lo usan la [diaria](diaria.md), a las 9:00, y la rutina «PRs», de lunes a viernes a las 12:00 y a las 17:00.

Conectores: GitHub, solo lectura.

## Qué cuenta

Una PR cuenta si cumple todo esto:

- está abierta y no es borrador;
- su base es `main`;
- está en uno de estos repos de `aie-online-tb`: `equipo-montes`, `bootcamp_AI_Engineering_10_26` o `material_bootcamp_AI_Engineering`;
- no la ha abierto la persona. Los usuarios de GitHub de cada uno están en `docs/mapa-recursos.md`. Las PRs que abre Claude desde la cuenta de alguien cuentan como de esa persona;
- la persona no la ha aprobado ya después del último commit.

## Qué dice de cada una

Una línea: repo, número y título con enlace, autor, cuánto lleva abierta y el estado de los checks (verde, rojo o en curso).

Va primero si es urgente:
- es la PR de `develop` a `main` del repo de alumnos y hoy es jueves por la mañana, porque es la liberación;
- lleva más de 24 horas abierta;
- tiene los checks en rojo, porque entonces no se debe mergear y hay que avisar a su autor.

## Cómo avisa

- En la diaria, como primer bloque, «PRs por revisar». Si no hay ninguna, no sale el bloque.
- En la rutina «PRs», con una notificación de la app de Claude solo si hay alguna. Si no hay, termina sin avisar.
- Nunca revisa, aprueba, comenta ni mergea: solo avisa.
