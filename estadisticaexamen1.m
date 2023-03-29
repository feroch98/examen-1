% Carga el archivo Excel
filename = 'excelexamen1.xlsx';
data = readtable(filename);

% Extrae las columnas 'estatura' y 'talla'
estatura = data.estatura;
talla = data.talla;
sexo = data.Sexo;

% Calcula la media y la desviación estándar de las columnas 'estatura' y 'talla'
media_estatura = mean(estatura);
std_estatura = std(estatura);
media_talla = mean(talla);
std_talla = std(talla);

% Ajusta una distribución normal a las curvas de las columnas 'estatura' y 'talla'
pd_estatura = fitdist(estatura, 'Normal');
pd_talla = fitdist(talla, 'Normal');

% Muestra los parámetros de las distribuciones ajustadas
disp(['Distribución ajustada para estatura: ', char(pd_estatura.DistributionName)]);
disp(['Media: ', num2str(pd_estatura.mu)]);
disp(['Desviación estándar: ', num2str(pd_estatura.sigma)]);

disp(['Distribución ajustada para talla: ', char(pd_talla.DistributionName)]);
disp(['Media: ', num2str(pd_talla.mu)]);
disp(['Desviación estándar: ', num2str(pd_talla.sigma)]);

% Imprime los histogramas y las funciones gaussiana ajustadas
figure;
subplot(2,2,1);
h1 = histogram(estatura, 'Normalization', 'pdf', 'EdgeColor', 'none');
hold on;
x1 = linspace(min(estatura), max(estatura), 100);
plot(x1, pdf(pd_estatura, x1), 'LineWidth', 2);
hold off;
title('Histograma de Estatura');
legend('Datos', 'Distribución ajustada');

subplot(2,2,2);
h2 = histogram(talla, 'Normalization', 'pdf', 'EdgeColor', 'none');
hold on;
x2 = linspace(min(talla), max(talla), 100);
plot(x2, pdf(pd_talla, x2), 'LineWidth', 2);
hold off;
title('Histograma de Talla');
legend('Datos', 'Distribución ajustada');

% Calcula la probabilidad de estar dentro de la primera desviación estándar
p_estatura = cdf(pd_estatura, pd_estatura.mu + pd_estatura.sigma) - cdf(pd_estatura, pd_estatura.mu - pd_estatura.sigma);
p_talla = cdf(pd_talla, pd_talla.mu + pd_talla.sigma) - cdf(pd_talla, pd_talla.mu - pd_talla.sigma);

% Muestra la probabilidad de estar dentro de la primera desviación estándar
disp(['La probabilidad de estar dentro de la primera desviación estándar para la estatura es: ', num2str(p_estatura)]);
disp(['La probabilidad de estar dentro de la primera desviación estándar para la talla es: ', num2str(p_talla)]);

% Ajusta una recta a los datos de estatura y talla para la población general
p = polyfit(estatura, talla, 1);
fit_talla = polyval(p, estatura);

% Muestra la recta ajustada y los datos de estatura y talla para la población general
figure;
plot(estatura, talla, 'o');
hold on;
plot(estatura, fit_talla, 'r-', 'LineWidth', 2);
xlabel('Estatura');
ylabel('Talla de calzado');
title('Ajuste lineal para la población general');
% Divide los datos por sexo y ajusta una recta a cada subgrupo
sexo_unique = unique(sexo);
figure;

for i = 1:length(sexo_unique)
    subplot(1, length(sexo_unique), i);
    index = sexo == sexo_unique(i);
    p = polyfit(estatura(index), talla(index), 1);
    fit_talla = polyval(p, estatura(index));
    plot(estatura(index), talla(index), 'o');
    hold on;
    plot(estatura(index), fit_talla, 'r-', 'LineWidth', 2);
    xlabel('Estatura');
    ylabel('Talla de calzado');
    title(['Ajuste lineal para ' sexo_unique{i}]);
end

