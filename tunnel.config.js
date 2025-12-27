module.exports = {
  apps : [{
    name: "aries-bridge",
    // Kita tunjuk langsung ke biner yang tadi lo install via NPM
    script: "/data/data/com.termux/files/usr/bin/ngrok",
    args: "http 3001 --url leakless-ongoing-daren.ngrok-free.dev",
    autorestart: true,
    // Tambahkan baris ini biar dia gak pake shell wrapper
    shell: false, 
    env: {
      HOME: "/data/data/com.termux/files/home",
      USER: "fauzan",
      NGROK_CONFIG: "/data/data/com.termux/files/home/.config/ngrok/ngrok.yml"
    }
  }]
}



