-- 코드를 작성해주세요
SELECT COUNT(ID) AS FISH_COUNT, MONTH(TIME) AS MONTH
FROM FISH_INFO
GROUP BY 2
ORDER BY 2