-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-03-2021 a las 21:15:36
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consulta`
--

CREATE TABLE `consulta` (
  `idConsulta` int(11) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  `categoria` varchar(30) NOT NULL,
  `descripcion` mediumtext NOT NULL,
  `importancia` varchar(30) NOT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `consulta`
--

INSERT INTO `consulta` (`idConsulta`, `idUsuario`, `categoria`, `descripcion`, `importancia`, `fecha`) VALUES
(6, 8, 'Proyecto de vida', 'esto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultesto es un defaultes', 'Media', '2021-03-11'),
(7, 29, 'Laboral', 'esta es la descripcion', 'Media', '2021-03-11');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `culto`
--

CREATE TABLE `culto` (
  `idCulto` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `horainicio` time(4) NOT NULL,
  `horafinal` time(4) NOT NULL,
  `capacidad` int(100) NOT NULL,
  `capacidadmax` int(100) NOT NULL,
  `piso` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `culto`
--

INSERT INTO `culto` (`idCulto`, `fecha`, `horainicio`, `horafinal`, `capacidad`, `capacidadmax`, `piso`) VALUES
(11, '2021-01-01', '07:00:00.0000', '08:00:00.0000', 1, 50, 1),
(13, '2021-01-14', '07:00:00.0000', '08:00:00.0000', 0, 30, 1),
(14, '2021-01-20', '13:00:00.0000', '14:00:00.0000', 0, 30, 1),
(15, '2021-02-01', '07:00:00.0000', '08:00:00.0000', 0, 30, 1),
(16, '2021-02-04', '17:00:00.0000', '18:00:00.0000', 0, 30, 1),
(17, '2021-02-10', '07:00:00.0000', '08:00:00.0000', 0, 30, 1),
(18, '2021-01-05', '05:05:00.0000', '06:06:00.0000', 0, 30, 1),
(19, '2021-01-06', '05:05:00.0000', '06:06:00.0000', 0, 30, 1),
(20, '2021-02-15', '06:06:00.0000', '06:08:00.0000', 0, 30, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reserva`
--

CREATE TABLE `reserva` (
  `idReserva` int(11) NOT NULL,
  `idCulto` int(11) NOT NULL,
  `IdUsuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `apellido` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `tipoDocumento` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `cedula` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `imagen` longblob DEFAULT NULL,
  `edad` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `genero` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `rh` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `tipoAsistente` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `correo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `celular` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `direccion` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `estadoCivil` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `epsSisben` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fechaBautizmo` date DEFAULT NULL,
  `pastorBautizo` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `llenoSanto` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` date DEFAULT NULL,
  `servidorLocal` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `comite` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cargo` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `privilegio` varchar(20) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `nombre`, `apellido`, `tipoDocumento`, `cedula`, `password`, `imagen`, `edad`, `fechaNacimiento`, `genero`, `rh`, `tipoAsistente`, `correo`, `celular`, `direccion`, `estadoCivil`, `epsSisben`, `fechaBautizmo`, `pastorBautizo`, `llenoSanto`, `fecha`, `servidorLocal`, `comite`, `cargo`, `privilegio`) VALUES
(1, 'Juan Diego', 'Caicedo', 'Cédula de Ciudadanía', '1007341626', '$2b$12$mIXzWpOLguvW.QUW05R.1OJ4DCZVxOvx/r1aUiwjqixQvjfMFpvJK', 0x666f746f2e6a7067, '20', '2000-07-10', 'Hombre', 'A+', 'Amigo Simpatizante', 'juandi1007@hotmail.com', '3213136597', 'calle 65b #88-97', 'Soltero/a', 'servimierda', '0000-00-00', '', 'No', '0000-00-00', 'no', '', '', '2'),
(8, 'c', 'c', 'Cédula de Ciudadanía', '1007415334', '$2b$12$mIXzWpOLguvW.QUW05R.1OJ4DCZVxOvx/r1aUiwjqixQvjfMFpvJK', 0x4872612e706e67, '20', '2000-06-08', 'Hombre', 'B+', 'hb', 'c@g.com', '1', '21', 'Soltero/a', '21', '2021-02-12', 'ss', 'si', '0000-00-00', 'si', 'sss', 'uncargo', '2'),
(28, 'Juan ', 'Caicedo', 'Cédula de Ciudadanía', '100734', '$2b$12$mIXzWpOLguvW.QUW05R.1OJ4DCZVxOvx/r1aUiwjqixQvjfMFpvJK', NULL, '20', '2000-07-10', 'Hombre', 'A+', 'Amigo Simpatizante', 'juandi1007@hotmail.com', '3213136597', 'calle 65b #88-97', 'Soltero/a', 'servimierda', '0000-00-00', '', 'No', '0000-00-00', 'no', '', '', '2'),
(29, 'user', 'us', 'Cédula de Ciudadanía', '100', '$2b$12$R37jNgXoZCFsuCMIjIJLFOQ7/KLx4y.2xiYiE6Afa7yRjIYj8Gss2', '', '0', '2020-10-08', 'Hombre', 'B+', 'as', 'c@g.com', '1', '21', 'Soltero/a', 'eps', '0000-00-00', '', 'si', '0000-00-00', 'no', '', '', '1');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`idConsulta`),
  ADD KEY `idUsuario` (`idUsuario`);

--
-- Indices de la tabla `culto`
--
ALTER TABLE `culto`
  ADD PRIMARY KEY (`idCulto`);

--
-- Indices de la tabla `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`idReserva`),
  ADD KEY `IdUsuario` (`IdUsuario`),
  ADD KEY `idCulto` (`idCulto`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `consulta`
--
ALTER TABLE `consulta`
  MODIFY `idConsulta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `culto`
--
ALTER TABLE `culto`
  MODIFY `idCulto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `reserva`
--
ALTER TABLE `reserva`
  MODIFY `idReserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `consulta`
--
ALTER TABLE `consulta`
  ADD CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`);

--
-- Filtros para la tabla `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `reserva_ibfk_1` FOREIGN KEY (`IdUsuario`) REFERENCES `usuarios` (`idUsuario`),
  ADD CONSTRAINT `reserva_ibfk_2` FOREIGN KEY (`idCulto`) REFERENCES `culto` (`idCulto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
