# Recomendaciones: Sigue el paso a paso, ya que si no es así, el Clips no tomará las definiciones.

# <---------- Paso#1 ---------->

```
(deftemplate animal
   (slot name)
)
```

# <---------- Paso#2 ---------->

```
(deftemplate animal-and-sound
   (slot animal-name)
   (slot sound)
)
```

# <---------- Paso#3 ---------->

```
(defrule assign-sound
   ?animal <- (animal (name ?name))
   =>
   (switch ?name
      (case duck then (assert (animal-and-sound (animal-name ?name) (sound Cuack))))
      (case dog then (assert (animal-and-sound (animal-name ?name) (sound Guau))))
      (case cat then (assert (animal-and-sound (animal-name ?name) (sound MIau))))
      (default (assert (animal-and-sound (animal-name ?name) (sound unknown))))
   )
   (retract ?animal)
)
```

# <---------- Paso#4 ---------->

# Ejemplos propuestos para añadir, según el caso: pato, perro, gato o en su defecto, el desconocido, para opciones que no se tienen en cuenta.
# Nota: También recomiendo pegarlos uno a uno, ya que de lo contrario, solo tomará el primero.

```
(assert (animal (name duck)))
(assert (animal (name dog)))
(assert (animal (name cat)))
(assert (animal (name elephant))) 
```

# <---------- Paso#5 ---------->
# Ver los hechos agregados antes de ejecutar la regla. (Aquí solo incluye el animal sin el sonido, ya que no ha sido expuesto a la regla).

```
(facts)
```

# <---------- Paso#6 ---------->
# Aquí vamos a ejecutar la regla, ya que en el paso anterior solo estamos dando el animal, y en este ya se evaluará según la regla dada para determinar el animal y asignar el sonido.

```
(run)
```

# <---------- Paso#6 ---------->
# Ver los hechos resultantes después de haber corrido la regla. (Aquí ya incluye los sonidos respectivos).

```
(facts)
```
