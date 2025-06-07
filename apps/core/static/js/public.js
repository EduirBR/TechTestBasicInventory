// Función para verificar si el usuario está autenticado y redirigir si es necesario
async function checkPublicAccess() {
    const accessToken = localStorage.getItem("accessToken");

    // Si hay token, verificar si es válido
    if (accessToken) {
        try {
            const response = await fetch("/api/token/verify", {
                method: "GET",
                headers: {
                    Authorization: `Bearer ${accessToken}`,
                    "Content-Type": "application/json",
                },
            });

            if (response.ok) {
                // Si el token es válido y estamos en una página pública, redirigir al dashboard
                if (
                    window.location.pathname === "/" ||
                    window.location.pathname.includes("/login") ||
                    window.location.pathname.includes("/register")
                ) {
                    window.location.href = "/dashboard";
                    return false;
                }
            } else {
                // Si el token no es válido, limpiarlo
                localStorage.removeItem("accessToken");
                localStorage.removeItem("refreshToken");
                return true;
            }
        } catch (error) {
            console.error("Error al verificar autenticación:", error);
            localStorage.removeItem("accessToken");
            localStorage.removeItem("refreshToken");
            return true;
        }
    }

    return true;
}

// Función para proteger páginas públicas
async function protectPublicPage() {
    const canAccess = await checkPublicAccess();
    return canAccess;
}

// Exportar las funciones para uso en otros archivos
window.publicUtils = {
    checkPublicAccess,
    protectPublicPage,
};
