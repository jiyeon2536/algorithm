-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B USING (ANIMAL_ID))
ORDER BY 1