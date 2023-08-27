(deftemplate plataforma-elegida
    (slot seleccion (type INTEGER)))

(deftemplate tipo-plataforma
    (slot tipo))

(deftemplate preferencias
    (slot accion (type INTEGER))
    (slot online (type INTEGER))
    (slot multijugador (type INTEGER))
    (slot estrategia (type INTEGER))
    (slot solitario (type INTEGER))
    (slot casuales (type INTEGER)))

;; Pregunta sobre la plataforma
(defrule pregunta-plataforma
    (not (plataforma-elegida))
    =>
    (printout t "¡Bienvenido! Este programa te ayudará a encontrar juegos que se acoplen a tus preferencias." crlf)
    (printout t "Por favor, responde 1 para Sí y 0 para No." crlf crlf)
    (printout t "¿En qué plataforma te gustaría jugar? (1: Consola, 2: Computadora, 3: Móvil): ")
    (bind ?plataforma (read))
    (if (or (= ?plataforma 1) (= ?plataforma 2) (= ?plataforma 3)) then
        (assert (plataforma-elegida (seleccion ?plataforma)))
        (switch ?plataforma
            (case 1 then (assert (tipo-plataforma (tipo consola))))
            (case 2 then (assert (tipo-plataforma (tipo computadora))))
            (case 3 then (assert (tipo-plataforma (tipo movil))))
        )
    )
)

;; Preguntas sobre preferencias de género de juego en consola
(defrule pregunta-gustos-consola
    (plataforma-elegida (seleccion 1))
    (not (preferencias (accion ?) (online ?) (multijugador ?)))
    =>
    (printout t "¿Te gustan los juegos de acción en consola? (1: Sí, 0: No): ")
    (bind ?accion (read))
    (printout t "¿Te gusta jugar en línea en tu consola? (1: Sí, 0: No): ")
    (bind ?online (read))
    (printout t "¿Prefieres juegos multijugador en tu consola? (1: Sí, 0: No): ")
    (bind ?multijugador (read))
    (assert (preferencias (accion ?accion) (online ?online) (multijugador ?multijugador)))
)

;; Preguntas adicionales sobre preferencias en computadora
(defrule pregunta-gustos-computadora
    (plataforma-elegida (seleccion 2))
    (not (preferencias (estrategia ?) (solitario ?)))
    =>
    (printout t "¿Te gustan los juegos de estrategia en computadora? (1: Sí, 0: No): ")
    (bind ?estrategia (read))
    (printout t "¿Te gustan los juegos de un jugador (solitario) en tu computadora? (1: Sí, 0: No): ")
    (bind ?solitario (read))
    (assert (preferencias (estrategia ?estrategia) (solitario ?solitario)))
)

;; Preguntas sobre preferencias en móvil
(defrule pregunta-gustos-movil
    (plataforma-elegida (seleccion 3))
    (not (preferencias (casuales ?)))
    =>
    (printout t "¿Te gustan los juegos casuales en móvil? (1: Sí, 0: No): ")
    (bind ?casuales (read))
    (assert (preferencias (casuales ?casuales)))
)

;; Reglas de recomendación
(defrule recomendacion-consola-accion
    (plataforma-elegida (seleccion 1))
    (preferencias (accion 1))
    =>
    (printout t "¡Te recomendamos probar 'The Last of Us Part II' y 'Ghost of Tsushima' en tu consola!" crlf)
)

(defrule recomendacion-consola-online
    (plataforma-elegida (seleccion 1))
    (preferencias (online 1))
    =>
    (printout t "¡Si te gusta jugar en línea, podrías disfrutar de 'Apex Legends' y 'Call of Duty: Warzone' en tu consola!" crlf)
)

(defrule recomendacion-consola-multijugador
    (plataforma-elegida (seleccion 1))
    (preferencias (multijugador 1))
    =>
    (printout t "¡Para experiencias multijugador, te sugerimos 'Overwatch' y 'Rocket League' en tu consola!" crlf)
)

(defrule recomendacion-computadora-estrategia
    (plataforma-elegida (seleccion 2))
    (preferencias (estrategia 1))
    =>
    (printout t "¡Te recomendamos jugar 'Sid Meier's Civilization VI' y 'Total War: Three Kingdoms' en tu computadora!" crlf)
)

(defrule recomendacion-computadora-solitario
    (plataforma-elegida (seleccion 2))
    (preferencias (solitario 1))
    =>
    (printout t "Si te gustan los juegos de un jugador, podrías disfrutar 'The Witcher 3: Wild Hunt' y 'Red Dead Redemption 2' en tu computadora." crlf)
)

(defrule recomendacion-movil-casuales
    (plataforma-elegida (seleccion 3))
    (preferencias (casuales 1))
    =>
    (printout t "¡Te recomendamos probar 'Among Us' y 'Clash Royale' en tu móvil!" crlf)
)

;; Combinar reglas y preguntas en la ejecución
(defrule mostrar-recomendacion
    (plataforma-elegida (seleccion ?plataforma))
    (preferencias (accion ?accion) (online ?online) (multijugador ?multijugador) (estrategia ?estrategia) (solitario ?solitario) (casuales ?casuales))
    =>
    (printout t "Basado en tus respuestas, te recomendamos los siguientes juegos:" crlf)
    (if (= ?accion 1) then (printout t "  - Juegos de acción" crlf))
    (if (= ?online 1) then (printout t "  - Juegos en línea" crlf))
    (if (= ?multijugador 1) then (printout t "  - Juegos multijugador" crlf))
    (if (= ?estrategia 1) then (printout t "  - Juegos de estrategia" crlf))
    (if (= ?solitario 1) then (printout t "  - Juegos de un jugador" crlf))
    (if (= ?casuales 1) then (printout t "  - Juegos casuales" crlf))
)

