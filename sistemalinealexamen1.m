A = [0.25 0.15 0; 0.45 0.5 0.75; 0.3 0.35 0.25];
b = [1.5; 5; 3];
x = linsolve(A, b);
fprintf('Cantidad de fertilizante tipo A: %.2f toneladas\n', x(1));
fprintf('Cantidad de fertilizante tipo B: %.2f toneladas\n', x(2));
fprintf('Cantidad de fertilizante tipo C: %.2f toneladas\n', x(3));

