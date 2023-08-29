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
    (slot puzzle (type INTEGER))

    (slot peleas (type INTEGER))
    (slot arcade (type INTEGER))
    (slot musicales (type INTEGER))
    (slot plataformas (type INTEGER))
    (slot Soulslikes (type INTEGER))
    (slot educativos (type INTEGER))
    (slot rompecabezas (type INTEGER))
    (slot mmorpg (type INTEGER))
    (slot mesa (type INTEGER))
    (slot cartas (type INTEGER))
    (slot velocidad (type INTEGER))
    (slot metroidvania (type INTEGER)))

(deftemplate recomendaciones-juegos
    (slot plataforma)
    (multislot juegos))

(deftemplate recomendaciones-hardware
    (slot plataforma)
    (slot ram)
    (slot rom)
    (slot disco)
    (slot procesador))


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
    (not (preferencias (accion ?) (multijugador ?) (terror ?) (deportes ?) (rol ?)
    (Soulslikes ?) (plataformas ?) (musicales ?) (arcade ?) (peleas ?)))
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
    (printout t "¿Te gustan los juegos de peleas en tu consola? (1: Sí, 0: No): ")
    (bind ?peleas (read))
    (printout t "¿Te gustan los juegos arcade en consola? (1: Sí, 0: No): ")
    (bind ?arcade (read)) 
    (printout t "¿Te gustan los juegos musicales en tu consola? (1: Sí, 0: No): ")
    (bind ?musicales (read))
    (printout t "¿Te gustan los juegos de plataformas en tu consola? (1: Sí, 0: No): ")
    (bind ?plataformas (read))
    (printout t "¿Te gustan los juegos tipo Soulslikes en tu consola? (1: Sí, 0: No): ")
    (bind ?Soulslikes (read))
    (assert (preferencias (accion ?accion) (multijugador ?multijugador) (terror ?terror) (deportes ?deportes) (rol ?rol)
        (Soulslikes ?Soulslikes) (plataformas ?plataformas) (musicales ?musicales) (arcade ?arcade) (peleas ?peleas))
    )
)

;; Preguntas adicionales sobre preferencias en computadora
(defrule pregunta-gustos-computadora
    (plataforma-elegida (seleccion 2))
    (not (preferencias (estrategia ?) (solitario ?) (simulador ?) (aventura ?) (royale ?)
        (metroidvania ?)(terror ?)(velocidad ?)(mmorpg ?)(deportes ?)))
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
    (printout t "¿Te gustan los juegos tipo metroidvania en tu computadora? (1: Sí, 0: No): ")
    (bind ?metroidvania (read))
    (printout t "¿Prefieres juegos de terror en tu computadora? (1: Sí, 0: No): ")
    (bind ?terror (read))
    (printout t "¿Prefieres juegos de carreras en tu computadora? (1: Sí, 0: No): ")
    (bind ?velocidad (read))
    (printout t "¿Te gustan los juegos MMORPG para móvil? (1: Sí, 0: No): ")
    (bind ?mmorpg (read))
    (printout t "¿Prefieres juegos de deportes en tu computadora? (1: Sí, 0: No): ")
    (bind ?deportes (read))
    (assert (preferencias (estrategia ?estrategia) (solitario ?solitario) (simulador ?simulador) (aventura ?aventura) (royale ?royale)
        (metroidvania ?metroidvania) (terror ?terror) (velocidad ?velocidad) (mmorpg ?mmorpg) (deportes ?deportes))
    )
)

;; Preguntas sobre preferencias en móvil
(defrule pregunta-gustos-movil
    (plataforma-elegida (seleccion 3))
    (not (preferencias (casuales ?) (multijugador ?) (estrategia ?) (deportes ?) (puzzle ?) (educativos ?) (mesa ?) (rompecabezas ?)(cartas ?)(mmorpg ?)))
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
     (printout t "¿Te gustan los juegos educativos en móvil? (1: Sí, 0: No): ")
    (bind ?educativos(read))
    (printout t "¿Te gustan los juegos de rompecabezas para móvil? (1: Sí, 0: No): ")
    (bind ?rompecabezas (read))
    (printout t "¿Te gustan los juegos de mesa para móvil? (1: Sí, 0: No): ")
    (bind ?mesa (read))
    (printout t "¿Te gustan los juegos de cartas para móvil? (1: Sí, 0: No): ")
    (bind ?cartas (read))
    (printout t "¿Te gustan los juegos MMORPG para móvil? (1: Sí, 0: No): ")
    (bind ?mmorpg (read))
    (assert (preferencias (casuales ?casuales)(multijugador ?multijugador)(estrategia ?estrategia)(deportes ?deportes)(puzzle ?puzzle)
    (educativos ?educativos)(mesa ?mesa)(cartas ?cartas)(rompecabezas ?rompecabezas)(mmorpg ?mmorpg)))
)

;; Reglas de recomendación
(defrule recomendacion-consola-accion
    (plataforma-elegida (seleccion 1))
    (preferencias (accion 1))
    =>
    (assert (recomendaciones-juegos (plataforma "Consola") (juegos "The Last of Us Part II" "Ghost of Tsushima")))
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

(defrule recomendacion-consola-peleas
    (plataforma-elegida (seleccion 1))
    (preferencias (peleas 1))
    =>
    (printout t "Si te gustan los juegos de peleas, podrías disfrutar 'Dragon Ball Z: Kakarot' y 'Mortal Kombat 11' en tu consola." crlf)
)

(defrule recomendacion-consola-plataformas
    (plataforma-elegida (seleccion 1))
    (preferencias (plataformas 1))
    =>
    (printout t "Si te gustan los juegos de plataformas, podrías disfrutar 'Super Mario Maker 2' y 'crash bandicoot 4' en tu consola." crlf)
)

(defrule recomendacion-consola-arcade
    (plataforma-elegida (seleccion 1))
    (preferencias (arcade 1))
    =>
    (printout t "Si te gustan los juegos arcade, podrías disfrutar 'Metal Slug 2' y 'Art of Rally' en tu consola." crlf)
)

(defrule recomendacion-consola-musicales
    (plataforma-elegida (seleccion 1))
    (preferencias (musicales 1))
    =>
    (printout t "Si te gustan los juegos musicales, podrías disfrutar 'Just Dance 2021' y 'Guitar Hero III' en tu consola." crlf)
)

(defrule recomendacion-consola-Soulslikes
    (plataforma-elegida (seleccion 1))
    (preferencias (Soulslikes 1))
    =>
    (printout t "Si te gustan los desafios, podrías disfrutar estos juegos tipo Soulslikes 'Elden Ring' y 'Bloodborne' en tu consola." crlf)
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

(defrule recomendacion-computadora-velocidad
    (plataforma-elegida (seleccion 2))
    (preferencias (velocidad 1))
    =>
    (printout t "¡Para experiencias de velocidad, podrías disfrutar de 'Need For Speed' y 'Forza Horizon 5' en tu computadora!." crlf)
)

(defrule recomendacion-computadora-metroidvania
    (plataforma-elegida (seleccion 2))
    (preferencias (metroidvania 1))
    =>
    (printout t "Te recomendamos jugar 'Blasphemous' y 'Ghost 1.0' en tu computadora." crlf)
)

(defrule recomendacion-computadora-terror
    (plataforma-elegida (seleccion 2))
    (preferencias (terror 1))
    =>
    (printout t "¡Para experiencias terrorificas, te sugerimos 'Silent Hill 2' y 'Resident Evil 4' en tu computadora!" crlf)
)


(defrule recomendacion-computadora-mmorpg
    (plataforma-elegida (seleccion 2))
    (preferencias (mmorpg 1))
    =>
    (printout t "¡Te sugerimos 'World of Warcraft' y 'Lineage II' en tu computadora!" crlf)
)

(defrule recomendacion-computadora-deportes
    (plataforma-elegida (seleccion 2))
    (preferencias (deportes 1))
    =>
    (printout t "¡Te recomendamos probar 'Fifa 23' y 'NBA 2K 22' en tu computadora!" crlf)
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

(defrule recomendacion-movil-educativos
    (plataforma-elegida (seleccion 3))
    (preferencias (educativos 1))
    =>
    (printout t "¡Te recomendamos probar 'MathLand' y 'MindX' en tu móvil!" crlf)
)

(defrule recomendacion-movil-mmorpg
    (plataforma-elegida (seleccion 3))
    (preferencias (mmorpg 1))
    =>
    (printout t "¡Te recomendamos probar 'Albion Online' y 'Genshin Impact' en tu móvil!" crlf)
)

(defrule recomendacion-movil-rompecabezas 
    (plataforma-elegida (seleccion 3))
    (preferencias (rompecabezas 1))
    =>
    (printout t "¡Te recomendamos probar 'Tiny Room Stories' y 'Bridge Construction' en tu móvil!" crlf)
)

(defrule recomendacion-movil-mesa
    (plataforma-elegida (seleccion 3))
    (preferencias (mesa 1))
    =>
    (printout t "¡Te recomendamos probar 'Monopoly' y 'Magnus Trainer' en tu móvil!" crlf)
)

(defrule recomendacion-movil-cartas
    (plataforma-elegida (seleccion 3))
    (preferencias (cartas 1))
    =>
    (printout t "¡Te recomendamos probar 'Yu-Gi-Oh Master Duel' y 'Hearthstone' en tu móvil!" crlf)
)

;; Regla para manejar el caso sin preferencias
(defrule no-recomendacion
    (plataforma-elegida (seleccion ?plataforma))
    (preferencias (accion 0) (multijugador 0) (terror 0) (deportes 0) (rol 0) (estrategia 0) (solitario 0) (simulador 0) (aventura 0) (royale 0) (casuales 0) (puzzle 0)
        (arcade 0) (musicales 0) (plataformas 0) (Soulslikes 0) (educativos 0) (rompecabezas 0) (mmorpg 0) (mesa 0) (cartas 0) (peleas 0) (velocidad 0) (metroidvania 0))
    =>
    (printout t "Lo sentimos, no podemos recomendarte juegos debido a que no seleccionaste ninguna preferencia." crlf)
)


;; Combinar reglas y preguntas en la ejecución
(defrule mostrar-recomendacion
    (plataforma-elegida (seleccion ?plataforma))
    (preferencias 
        (accion ?accion)
        (multijugador ?multijugador)
        (terror ?terror)
        (deportes ?deportes)
        (rol ?rol)
        (estrategia ?estrategia)
        (solitario ?solitario)
        (simulador ?simulador)
        (aventura ?aventura)
        (royale ?royale)
        (casuales ?casuales)
        (puzzle ?puzzle)
        (educativos ?educativos)
        (mesa ?mesa)
        (cartas ?cartas)
        (rompecabezas ?rompecabezas)
        (mmorpg ?mmorpg)
        (Soulslikes ?Soulslikes) 
        (plataformas ?plataformas) 
        (musicales ?musicales) 
        (arcade ?arcade) 
        (peleas ?peleas)
        (velocidad ?velocidad)
        (metroidvania ?metroidvania)
    )
    =>
    (printout t "Basado en tus respuestas, te recomendamos los siguientes componentes para tu plataforma " ?plataforma ":" crlf)
    (switch ?plataforma
        (case 1 then
            (bind ?ram-recomendada (+ ?accion ?multijugador ?terror ?deportes ?rol ?estrategia ?solitario ?simulador ?aventura ?royale ?casuales ?puzzle    
                ?arcade ?musicales ?plataformas ?Soulslikes ?educativos ?rompecabezas ?mmorpg ?mesa ?cartas ?peleas ?velocidad ?metroidvania))
            (bind ?almacenamiento-recomendado (* ?ram-recomendada 128))
            (printout t "  - RAM recomendada: " ?ram-recomendada " GB" crlf)
            (printout t "  - ROM recomendado (almacenamiento interno): " ?almacenamiento-recomendado " GB" crlf)
            (printout t "  - Disco duro recomendado: 1 TB" crlf)
            (printout t "  - Procesador recomendado: Quad-core" crlf))
        (case 2 then
            (bind ?ram-recomendada (+ ?accion ?multijugador ?terror ?deportes ?rol ?estrategia ?solitario ?simulador ?aventura ?royale ?casuales ?puzzle    
                ?arcade ?musicales ?plataformas ?Soulslikes ?educativos ?rompecabezas ?mmorpg ?mesa ?cartas ?peleas ?velocidad ?metroidvania))
            (bind ?almacenamiento-recomendado (* ?ram-recomendada 64))
            (printout t "  - RAM recomendada: " ?ram-recomendada " GB" crlf)
            (printout t "  - ROM recomendado (almacenamiento interno): " ?almacenamiento-recomendado " GB" crlf)
            (printout t "  - Disco duro recomendado: 1 TB" crlf)
            (printout t "  - Procesador recomendado: Intel Core i7" crlf))
        (case 3 then
            (bind ?ram-recomendada (+ ?accion ?multijugador ?terror ?deportes ?rol ?estrategia ?solitario ?simulador ?aventura ?royale ?casuales ?puzzle
                            ?arcade ?musicales ?plataformas ?Soulslikes ?educativos ?rompecabezas ?mmorpg ?mesa ?cartas ?peleas ?velocidad ?metroidvania))
            (bind ?almacenamiento-recomendado (* ?ram-recomendada 32))
            (printout t "  - RAM recomendada: " ?ram-recomendada " GB" crlf)
            (printout t "  - ROM recomendado (almacenamiento interno): " ?almacenamiento-recomendado " GB" crlf)
            (printout t "  - Procesador recomendado: Octa-core" crlf)))
    (printout t "Estos componentes te proporcionarán una experiencia óptima para una variedad de géneros de juegos." crlf)
)

