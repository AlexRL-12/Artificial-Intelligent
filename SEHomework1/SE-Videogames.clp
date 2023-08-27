(deftemplate plataforma-elegida
    (slot seleccion (type INTEGER)))

(deftemplate tipo-plataforma
    (slot tipo))

(deftemplate preferencias
    (slot accion (type INTEGER))
    (slot rol (type INTEGER))
    (slot terror (type INTEGER))
    (slot simulador (type INTEGER))
    (slot royale (type INTEGER))
    (slot aventura (type INTEGER))
    (slot multijugador (type INTEGER))
    (slot estrategia (type INTEGER))
    (slot solitario (type INTEGER))
    (slot casuales (type INTEGER))
    (slot deportes (type INTEGER))
    (slot puzzle (type INTEGER)))

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
    (not (preferencias (accion ?) (multijugador ?) (terror ?) (deportes ?) (rol ?)))
    =>
    (printout t "¿Te gustan los juegos de acción en consola? (1: Sí, 0: No): ")
    (bind ?accion (read))
    (printout t "¿Prefieres juegos multijugador en tu consola? (1: Sí, 0: No): ")
    (bind ?multijugador (read))
    (printout t "¿Prefieres juegos de terror en tu consola? (1: Sí, 0: No): ")
    (bind ?terror (read))
    (printout t "¿Prefieres juegos de deportes en tu consola? (1: Sí, 0: No): ")
    (bind ?deportes (read))
    (printout t "¿Prefieres juegos de rol (rpg) en tu consola? (1: Sí, 0: No): ")
    (bind ?rol (read))
    (assert (preferencias (accion ?accion) (multijugador ?multijugador) (terror ?terror) (deportes ?deportes) (rol ?rol)))
)

;; Preguntas adicionales sobre preferencias en computadora
(defrule pregunta-gustos-computadora
    (plataforma-elegida (seleccion 2))
    (not (preferencias (estrategia ?) (solitario ?) (simulador ?) (aventura ?) (royale ?)))
    =>
    (printout t "¿Te gustan los juegos de estrategia en computadora? (1: Sí, 0: No): ")
    (bind ?estrategia (read))
    (printout t "¿Te gustan los juegos de un jugador (solitario) en tu computadora? (1: Sí, 0: No): ")
    (bind ?solitario (read))
    (printout t "¿Te gustan los juegos de simulacion en tu computadora? (1: Sí, 0: No): ")
    (bind ?simulador (read))
    (printout t "¿Te gustan los juegos de aventura en tu computadora? (1: Sí, 0: No): ")
    (bind ?aventura (read))
    (printout t "¿Te gustan los juegos battle royale en tu computadora? (1: Sí, 0: No): ")
    (bind ?royale (read))
    (assert (preferencias (estrategia ?estrategia) (solitario ?solitario) (simulador ?simulador) (aventura ?aventura) (royale ?royale)))
)

;; Preguntas sobre preferencias en móvil
(defrule pregunta-gustos-movil
    (plataforma-elegida (seleccion 3))
    (not (preferencias (casuales ?) (multijugador ?) (estrategia ?) (deportes ?) (puzzle ?)))
    =>
    (printout t "¿Te gustan los juegos casuales en móvil? (1: Sí, 0: No): ")
    (bind ?casuales (read))
    (printout t "¿Te gustan los juegos multijugador en móvil? (1: Sí, 0: No): ")
    (bind ?multijugador (read))
    (printout t "¿Te gustan los juegos de estrategia en móvil? (1: Sí, 0: No): ")
    (bind ?estrategia (read))
    (printout t "¿Te gustan los juegos de deportes para móvil? (1: Sí, 0: No): ")
    (bind ?deportes (read))
    (printout t "¿Te gustan los juegos de puzzle para móvil? (1: Sí, 0: No): ")
    (bind ?puzzle (read))
    (assert (preferencias (casuales ?casuales)(multijugador ?multijugador)(estrategia ?estrategia)(deportes ?deportes)(puzzle ?puzzle)))
)

;; Reglas de recomendación
(defrule recomendacion-consola-accion
    (plataforma-elegida (seleccion 1))
    (preferencias (accion 1))
    =>
    (printout t "¡Te recomendamos probar 'The Last of Us Part II' y 'Ghost of Tsushima' en tu consola!" crlf)
)

(defrule recomendacion-consola-multijugador
    (plataforma-elegida (seleccion 1))
    (preferencias (multijugador 1))
    =>
    (printout t "¡Para experiencias multijugador, podrías disfrutar de 'Apex Legends' y 'Call of Duty: Warzone' en tu consola!" crlf)
)

(defrule recomendacion-consola-terror
    (plataforma-elegida (seleccion 1))
    (preferencias (terror 1))
    =>
    (printout t "¡Para experiencias terrorificas, te sugerimos 'Alien: Isolation' y 'Dead Space' en tu consola!" crlf)
)

(defrule recomendacion-consola-deportes
    (plataforma-elegida (seleccion 1))
    (preferencias (deportes 1))
    =>
    (printout t "¡Te recomendamos probar 'Fifa 23' y 'NBA 2K 22' en tu consola!" crlf)
)

(defrule recomendacion-consola-rol
    (plataforma-elegida (seleccion 1))
    (preferencias (rol 1))
    =>
    (printout t "¡para experiencias en juegos rpg, te sugerimos 'Dark Souls' y 'Final Fantasy VII Remake' en tu consola!" crlf)
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

(defrule recomendacion-computadora-simulador
    (plataforma-elegida (seleccion 2))
    (preferencias (simulador 1))
    =>
    (printout t "Si te gustan los simuladores, podrías disfrutar 'American Truck Simulator' y 'Los Sims 4' en tu computadora." crlf)
)

(defrule recomendacion-computadora-aventura
    (plataforma-elegida (seleccion 2))
    (preferencias (aventura 1))
    =>
    (printout t "Te recomendamos jugar 'No Man's Sky' y 'The Elder Scrolls V: Skyrim' en tu computadora." crlf)
)

(defrule recomendacion-computadora-royale
    (plataforma-elegida (seleccion 2))
    (preferencias (royale 1))
    =>
    (printout t "Si te gustan los battle royale, te recomendamos 'PUBG: Battlegrounds' y 'TFall Guys: Ultimate Knockout' en tu computadora." crlf)
)

(defrule recomendacion-movil-casuales
    (plataforma-elegida (seleccion 3))
    (preferencias (casuales 1))
    =>
    (printout t "¡Te recomendamos probar 'Among Us' y 'Clash Royale' en tu móvil!" crlf)
)

(defrule recomendacion-movil-multijugador
    (plataforma-elegida (seleccion 3))
    (preferencias (multijugador 1))
    =>
    (printout t "¡Te recomendamos probar 'Call of Duty: Mobile' y 'Genshin Impact' en tu móvil!" crlf)
)

(defrule recomendacion-movil-estrategia
    (plataforma-elegida (seleccion 3))
    (preferencias (estrategia 1))
    =>
    (printout t "¡Te recomendamos probar 'Plants vs Zombies' y 'Lords Mobile' en tu móvil!" crlf)
)

(defrule recomendacion-movil-deportes
    (plataforma-elegida (seleccion 3))
    (preferencias (deportes 1))
    =>
    (printout t "¡Te recomendamos probar 'eFootball 2023' y 'NBA 2K Mobile' en tu móvil!" crlf)
)

(defrule recomendacion-movil-puzzle
    (plataforma-elegida (seleccion 3))
    (preferencias (puzzle 1))
    =>
    (printout t "¡Te recomendamos probar 'Monument Valley' y 'The Room' en tu móvil!" crlf)
)

;; Combinar reglas y preguntas en la ejecución
(defrule mostrar-recomendacion
    (plataforma-elegida (seleccion ?plataforma))
    (preferencias (accion ?accion) (multijugador ?multijugador) (terror ?terror) (deportes ?deportes) (rol ?rol) (estrategia ?estrategia) (solitario ?solitario) (simulador ?simulador) (aventura ?aventura) (royale ?royale) (casuales ?casuales) (puzzle ?puzzle)
    )
    =>
    (printout t "Basado en tus respuestas, te recomendamos los siguientes juegos:" crlf)
    (if (= ?accion 1) then (printout t "  - Juegos de acción" crlf))
    (if (= ?multijugador 1) then (printout t "  - Juegos multijugador" crlf))
    (if (= ?terror 1) then (printout t "  - Juegos de terror" crlf))
    (if (= ?deportes 1) then (printout t "  - Juegos de deportes" crlf))
    (if (= ?rol 1) then (printout t "  - Juegos rpg" crlf))

    (if (= ?estrategia 1) then (printout t "  - Juegos de estrategia" crlf))
    (if (= ?solitario 1) then (printout t "  - Juegos de un jugador" crlf))
    (if (= ?simulador 1) then (printout t "  - Juegos de simulacion" crlf))
    (if (= ?aventura 1) then (printout t "  - Juegos de aventura" crlf))
    (if (= ?royale 1) then (printout t "  - Juegos battle royale" crlf))

    (if (= ?casuales 1) then (printout t "  - Juegos casuales" crlf))
    (if (= ?puzzle 1) then (printout t "  - Juegos puzzle" crlf))
)
