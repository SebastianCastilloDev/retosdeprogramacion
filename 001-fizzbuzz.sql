-- Escribe un programa que muestre por consola (con un print) los
-- números de 1 a 100 (ambos incluidos y con un salto de línea entre
-- cada impresión), sustituyendo los siguientes:
-- - Múltiplos de 3 por la palabra "fizz".
-- - Múltiplos de 5 por la palabra "buzz".
-- - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


WITH RECURSIVE Numbers AS (
  SELECT 1 AS num
  UNION ALL
  SELECT num + 1
  FROM Numbers
  WHERE num < 100
)
SELECT
  CASE
    WHEN num % 3 = 0 AND num % 5 = 0 THEN 'fizzbuzz'
    WHEN num % 3 = 0 THEN 'fizz'
    WHEN num % 5 = 0 THEN 'buzz'
    ELSE CAST(num AS VARCHAR)
  END AS result
FROM Numbers;
