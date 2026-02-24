/**
 * FEAC Service untuk sinkronisasi dengan Aries Intelligence (Port 3333/3001)
 */
const ARIES_URL = 'http://localhost:3333'; // Sesuaikan ke 3001 jika port aktif di sana

export const AriesService = {
    async getIntelligence() {
        console.log("🧠 [FEAC <- ARIES] Menarik logika cerdas dari 3333...");
        try {
            const response = await fetch(`${ARIES_URL}/api/logic`);
            return await response.json();
        } catch (error) {
            console.error("❌ Aries Intelligence Core Tidak Merespon");
        }
    }
};
