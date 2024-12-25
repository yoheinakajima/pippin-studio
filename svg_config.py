# svg_config.py

EXAMPLE_SVGS = {
    "pippin_the_unicorn": """<?xml version="1.0" encoding="UTF-8"?>
<svg width="250" height="250" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <g id="Unicorn_base_character">
      <!-- Legs -->
      <g>
        <path d="M100,160 L100,190" stroke="#000" stroke-width="2"/>
        <path d="M120,160 L120,190" stroke="#000" stroke-width="2"/>
        <path d="M140,160 L140,190" stroke="#000" stroke-width="2"/>
        <path d="M160,120 Q165,140 160,160" stroke="#000" stroke-width="2"/>
        <ellipse cx="100" cy="190" rx="5" ry="2" fill="#000"/>
        <ellipse cx="120" cy="190" rx="5" ry="2" fill="#000"/>
        <ellipse cx="140" cy="190" rx="5" ry="2" fill="#000"/>
        <ellipse cx="160" cy="160" rx="5" ry="2" fill="#000"/>
      </g>
      <!-- Body -->
      <g>
        <animateTransform
          attributeName="transform"
          attributeType="XML"
          type="translate"
          values="0 0; 0 10; 0 0"
          dur="1.2s"
          repeatCount="indefinite"
          calcMode="spline"
          keySplines="0.4 0 0.6 1; 0.4 0 0.6 1"/>
        <path d="M80,150 Q60,120 80,90 Q100,60 140,70 Q180,80 160,120 Q150,160 100,160 Z"
              fill="#fff" stroke="#000" stroke-width="2"/>
        <path d="M80,150 Q70,155 75,160 Q70,165 80,170" stroke="#ff69b4" stroke-width="2" fill="none"/>
        <path d="M75,160 Q80,165 75,170" stroke="#ff69b4" stroke-width="2" fill="none"/>
        <path d="M90,120 Q95,110 100,120" stroke="#000" stroke-width="1" fill="none"/>
        <path d="M110,130 Q115,120 120,130" stroke="#000" stroke-width="1" fill="none"/>
      </g>
      <!-- Head -->
      <g>
        <animateTransform
          attributeName="transform"
          attributeType="XML"
          type="translate"
          values="0 0; 0 8; 0 0"
          dur="1.2s"
          begin="0.1s"
          repeatCount="indefinite"
          calcMode="spline"
          keySplines="0.4 0 0.6 1; 0.4 0 0.6 1"/>
        <path d="M140,70 Q150,60 160,55 Q170,50 175,60 Q180,70 170,80 Q160,85 150,80 Q140,75 140,70 Z"
              fill="#fff" stroke="#000" stroke-width="2"/>
        <polygon points="160,55 155,35 165,35" fill="#ffd700" stroke="#000" stroke-width="1"/>
        <path d="M165,45 Q166,40 160,43" fill="#fff" stroke="#000" stroke-width="1"/>
        <path d="M170,45 Q171,40 165,43" fill="#fff" stroke="#000" stroke-width="1"/>
        <circle cx="162" cy="60" r="3" fill="#000"/>
        <circle cx="158" cy="60" r="1.5" fill="#fff"/>
        <path d="M155,55 Q150,60 155,65 Q150,70 155,75 Q150,80 155,85" stroke="#ff69b4" stroke-width="2" fill="none"/>
        <path d="M160,55 Q155,60 160,65 Q155,70 160,75 Q155,80 160,85" stroke="#ff69b4" stroke-width="2" fill="none"/>
      </g>
    </g>
  </defs>
  <use href="#Unicorn_base_character"/>
</svg>
"""
    # You can add more characters here, like:
    # "dragon": """<?xml ...>""",
    # "princess": """<?xml ...>""",
}
