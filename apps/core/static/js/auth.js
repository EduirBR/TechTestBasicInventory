// Función para verificar la autenticación y proteger rutas
async function checkAuth() {
    const accessToken = localStorage.getItem("accessToken");

    // Si no hay token, redirigir a login (excepto si ya estamos en login)
    if (!accessToken && !window.location.pathname.includes("/login")) {
        window.location.href = "/login";
        return false;
    }

    try {
        // Verificar el token con el endpoint de validación
        const response = await fetch("/api/token/verify", {
            method: "GET",
            headers: {
                Authorization: `Bearer ${accessToken}`,
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            // Si el token no es válido, limpiar localStorage y redirigir a login
            localStorage.removeItem("accessToken");
            localStorage.removeItem("refreshToken");
            if (!window.location.pathname.includes("/login")) {
                window.location.href = "/login";
            }
            return false;
        }

        return true;
    } catch (error) {
        console.error("Error al verificar autenticación:", error);
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");
        if (!window.location.pathname.includes("/login")) {
            window.location.href = "/login";
        }
        return false;
    }
}

// Función para proteger una página
async function protectPage() {
    const isAuthenticated = await checkAuth();
    if (!isAuthenticated) {
        return false;
    }
    return true;
}

// Función para cerrar sesión
async function logout() {
    try {
        // Primero eliminar los tokens
        localStorage.clear(); // Elimina todos los items del localStorage
        // Redirigir al endpoint de logout
        window.location.href = "/logout";
    } catch (error) {
        console.error("Error al cerrar sesión:", error);
        // Si hay un error, forzar la redirección
        window.location.href = "/login";
    }
}

// Exportar las funciones para uso en otros archivos
window.authUtils = {
    checkAuth,
    protectPage,
    logout,
};
