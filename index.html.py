<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
  <meta name="theme-color" content="#080f1a">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Taï Chi">
  <link rel="manifest" href="manifest.json">
  <link rel="apple-touch-icon" href="icon.png">
  <title>Taï Chi sur Chaise</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }

    body {
      font-family: 'Segoe UI', sans-serif;
      background: #080f1a;
      color: #d8eaf8;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* ── ÉCRAN ACCUEIL ── */
    #screen-home {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      flex: 1;
      padding: 30px 20px;
      text-align: center;
    }

    #screen-home h1 {
      font-size: 2em;
      color: #7ecfff;
      letter-spacing: 3px;
      margin-bottom: 8px;
    }

    #screen-home p {
      color: #557a99;
      font-size: 0.88em;
      margin-bottom: 40px;
      font-style: italic;
    }

    .btn-start {
      background: linear-gradient(135deg, #0d6eaa, #0a4a7a);
      color: #fff;
      border: none;
      border-radius: 50px;
      padding: 18px 50px;
      font-size: 1.1em;
      font-weight: bold;
      letter-spacing: 2px;
      cursor: pointer;
      box-shadow: 0 6px 30px rgba(14,110,170,0.4);
      transition: transform 0.15s, box-shadow 0.15s;
    }
    .btn-start:active { transform: scale(0.96); box-shadow: none; }

    .exercise-count {
      margin-top: 24px;
      color: #2a5a7a;
      font-size: 0.82em;
    }

    /* ── ÉCRAN EXERCICE ── */
    #screen-exercise {
      display: none;
      flex-direction: column;
      flex: 1;
    }

    .ex-header {
      background: #0d1a28;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #122033;
    }

    .ex-header .back-btn {
      background: none;
      border: none;
      color: #557a99;
      font-size: 1.4em;
      cursor: pointer;
      padding: 4px 10px 4px 0;
    }

    .ex-header .progress-text {
      font-size: 0.82em;
      color: #557a99;
    }

    .progress-bar-wrap {
      background: #0d1a28;
      padding: 0 20px 10px;
    }

    .progress-bar-bg {
      background: #122033;
      border-radius: 10px;
      height: 5px;
      overflow: hidden;
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #0d6eaa, #7ecfff);
      border-radius: 10px;
      transition: width 0.4s ease;
    }

    .ex-body {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px 20px 10px;
      overflow-y: auto;
    }

    .ex-num {
      font-size: 0.78em;
      color: #2a5a7a;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }

    .ex-name {
      font-size: 1.4em;
      font-weight: 700;
      color: #b8dff5;
      text-align: center;
      margin-bottom: 20px;
    }

    .ex-gif {
      width: 100%;
      max-width: 320px;
      aspect-ratio: 4/3;
      object-fit: cover;
      border-radius: 16px;
      border: 1px solid #1a3348;
      margin-bottom: 20px;
      background: #0d1a28;
    }

    .ex-reps {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #0a2a1e;
      border: 1px solid #1a6640;
      border-radius: 30px;
      padding: 10px 24px;
      margin-bottom: 16px;
    }

    .ex-reps .reps-icon { font-size: 1.2em; }

    .ex-reps .reps-label {
      color: #4dffa0;
      font-weight: bold;
      font-size: 1em;
    }

    .ex-tip {
      background: #0d1f30;
      border-left: 3px solid #0d6eaa;
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 0.84em;
      color: #7aadcc;
      line-height: 1.5;
      width: 100%;
      max-width: 360px;
      margin-bottom: 10px;
    }

    /* ── NAVIGATION BAS ── */
    .ex-nav {
      display: flex;
      gap: 12px;
      padding: 16px 20px 28px;
      background: #080f1a;
      border-top: 1px solid #0d1a28;
    }

    .btn-prev, .btn-next {
      flex: 1;
      border: none;
      border-radius: 14px;
      padding: 16px;
      font-size: 1em;
      font-weight: bold;
      cursor: pointer;
      transition: transform 0.15s;
    }
    .btn-prev:active, .btn-next:active { transform: scale(0.96); }

    .btn-prev {
      background: #0d1a28;
      color: #557a99;
      border: 1px solid #122033;
    }

    .btn-next {
      background: linear-gradient(135deg, #0d6eaa, #0a4a7a);
      color: #fff;
      box-shadow: 0 4px 20px rgba(14,110,170,0.3);
    }

    /* ── ÉCRAN FIN ── */
    #screen-end {
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      flex: 1;
      text-align: center;
      padding: 30px 24px;
    }

    #screen-end .end-icon { font-size: 4em; margin-bottom: 16px; }
    #screen-end h2 { color: #7ecfff; font-size: 1.6em; margin-bottom: 10px; }
    #screen-end p { color: #557a99; font-size: 0.9em; margin-bottom: 36px; line-height: 1.6; }

    .btn-restart {
      background: linear-gradient(135deg, #0d6eaa, #0a4a7a);
      color: #fff;
      border: none;
      border-radius: 50px;
      padding: 16px 44px;
      font-size: 1em;
      font-weight: bold;
      cursor: pointer;
      box-shadow: 0 6px 24px rgba(14,110,170,0.35);
    }
  </style>
</head>
<body>

<!-- ══ ÉCRAN ACCUEIL ══ -->
<div id="screen-home">
  <h1>🪑 Taï Chi</h1>
  <p>Exercices sur chaise · 12 mouvements doux</p>
  <button class="btn-start" onclick="startSession()">Commencer ▶</button>
  <div class="exercise-count">12 exercices · ~20 minutes</div>
</div>

<!-- ══ ÉCRAN EXERCICE ══ -->
<div id="screen-exercise">
  <div class="ex-header">
    <button class="back-btn" onclick="goHome()">← Accueil</button>
    <span class="progress-text" id="progress-text">1 / 12</span>
  </div>
  <div class="progress-bar-wrap">
    <div class="progress-bar-bg">
      <div class="progress-bar-fill" id="progress-fill" style="width:8%"></div>
    </div>
  </div>
  <div class="ex-body">
    <div class="ex-num" id="ex-num">Exercice 1</div>
    <div class="ex-name" id="ex-name">—</div>
    <img class="ex-gif" id="ex-gif" src="" alt="Animation exercice">
    <div class="ex-reps">
      <span class="reps-icon">🔄</span>
      <span class="reps-label" id="ex-reps">—</span>
    </div>
    <div class="ex-tip" id="ex-tip">—</div>
  </div>
  <div class="ex-nav">
    <button class="btn-prev" id="btn-prev" onclick="prevExercise()">◀ Précédent</button>
    <button class="btn-next" id="btn-next" onclick="nextExercise()">Suivant ▶</button>
  </div>
</div>

<!-- ══ ÉCRAN FIN ══ -->
<div id="screen-end">
  <div class="end-icon">🌿</div>
  <h2>Séance terminée !</h2>
  <p>Bravo, vous avez complété les 12 exercices.<br>Prenez un moment pour ressentir le calme.</p>
  <button class="btn-restart" onclick="goHome()">↩ Recommencer</button>
</div>

<script>
  const exercises = [
    {
      name: "Respiration du ventre",
      reps: "5 – 8 cycles",
      gif: "https://media1.giphy.com/media/csnDXB70VCgK6DbUZ7/200.gif",
      tip: "Inspirez en gonflant le ventre, expirez en le rentrant. Yeux mi-clos, corps relâché."
    },
    {
      name: "Lever les mains",
      reps: "8 fois",
      gif: "https://media2.giphy.com/media/gjU7BibnocUHmoJw1j/200.gif",
      tip: "Mains montent lentement paumes vers le haut, puis redescendent. Respirez en rythme."
    },
    {
      name: "Étirement latéral",
      reps: "6 × chaque côté",
      gif: "https://media2.giphy.com/media/Jmy25dpC0qdjpfYOQ6/200.gif",
      tip: "Arc de cercle doux vers la gauche, puis la droite. Ne forcez pas l'amplitude."
    },
    {
      name: "Balancement des bras",
      reps: "10 fois",
      gif: "https://media4.giphy.com/media/SzlkrRcjBHor89MhBQ/200.gif",
      tip: "Bras souples qui oscillent en suivant la rotation du buste. Comme des ailes légères."
    },
    {
      name: "Séparer la crinière du cheval",
      reps: "8 fois",
      gif: "https://media2.giphy.com/media/HL8dQP1mSK7UbCooqi/200.gif",
      tip: "Une main monte paume vers le ciel, l'autre descend. Alternance fluide et lente."
    },
    {
      name: "Queue de l'oiseau",
      reps: "6 – 8 fois",
      gif: "https://media4.giphy.com/media/c2JMrlFNRR8SDVpT1S/200.gif",
      tip: "Bras décrivent une courbe douce vers l'avant. Poignets souples, épaules basses."
    },
    {
      name: "Grue blanche déploie ses ailes",
      reps: "6 × chaque côté",
      gif: "https://media3.giphy.com/media/FOtXG7DgQqfghsZw3C/200.gif",
      tip: "Un bras monte (aile haute), l'autre descend (aile basse). Puis inversez doucement."
    },
    {
      name: "Torsion du buste",
      reps: "8 fois",
      gif: "https://media1.giphy.com/media/jTNuQdYbWGuApRcv7j/200.gif",
      tip: "Rotation lente du buste gauche-droite. Les hanches restent fixes, regard suit le mouvement."
    },
    {
      name: "Cercles des poignets",
      reps: "8 × chaque sens",
      gif: "https://media3.giphy.com/media/8K4oCp32DuxII9JPdl/200.gif",
      tip: "Bras légèrement levés. Grands cercles lents vers l'intérieur, puis vers l'extérieur."
    },
    {
      name: "Rouler les bras – Nuages",
      reps: "8 – 10 fois",
      gif: "https://media2.giphy.com/media/9AbW3ljwzc2Dzv1yZW/200.gif",
      tip: "Les bras roulent lentement l'un après l'autre, comme des nuages qui passent."
    },
    {
      name: "Pousser la montagne",
      reps: "8 fois",
      gif: "https://media3.giphy.com/media/RmfRsq0wML9UT9jPpH/200.gif",
      tip: "Paumes vers l'avant, poussez lentement devant vous, puis ramenez. Expirez en poussant."
    },
    {
      name: "Relâchement final",
      reps: "1 – 2 minutes",
      gif: "https://media1.giphy.com/media/YOwchcZiCSA7NwUuP8/200.gif",
      tip: "Mains sur les cuisses. Relâchez chaque partie du corps de la tête aux pieds. Respirez librement."
    }
  ];

  let current = 0;

  function showScreen(id) {
    ['screen-home','screen-exercise','screen-end'].forEach(s => {
      document.getElementById(s).style.display = 'none';
    });
    document.getElementById(id).style.display = 'flex';
  }

  function startSession() {
    current = 0;
    renderExercise();
    showScreen('screen-exercise');
  }

  function goHome() {
    showScreen('screen-home');
  }

  function renderExercise() {
    const ex = exercises[current];
    const total = exercises.length;
    document.getElementById('ex-num').textContent = `Exercice ${current + 1}`;
    document.getElementById('ex-name').textContent = ex.name;
    document.getElementById('ex-gif').src = ex.gif;
    document.getElementById('ex-reps').textContent = ex.reps;
    document.getElementById('ex-tip').textContent = ex.tip;
    document.getElementById('progress-text').textContent = `${current + 1} / ${total}`;
    document.getElementById('progress-fill').style.width = `${((current + 1) / total) * 100}%`;
    document.getElementById('btn-prev').style.opacity = current === 0 ? '0.3' : '1';
    document.getElementById('btn-next').textContent = current === total - 1 ? 'Terminer ✓' : 'Suivant ▶';
  }

  function nextExercise() {
    if (current < exercises.length - 1) {
      current++;
      renderExercise();
    } else {
      showScreen('screen-end');
    }
  }

  function prevExercise() {
    if (current > 0) {
      current--;
      renderExercise();
    }
  }

  // ── Service Worker (PWA offline)
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js');
  }
</script>
</body>
</html>