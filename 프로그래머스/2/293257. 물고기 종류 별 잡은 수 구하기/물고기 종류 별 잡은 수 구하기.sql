-- 코드를 작성해주세요
SELECT COUNT(a.ID) AS FISH_COUNT, FISH_NAME
FROM FISH_INFO a JOIN FISH_NAME_INFO b ON b.FISH_TYPE = a.FISH_TYPE
GROUP BY FISH_NAME
ORDER BY 1 DESC