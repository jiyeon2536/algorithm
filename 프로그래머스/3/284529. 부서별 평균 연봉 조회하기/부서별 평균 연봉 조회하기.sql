-- 코드를 작성해주세요
SELECT DEPT_ID, DEPT_NAME_EN, ROUND(AVG(SAL)) AS AVG_SAL
FROM HR_DEPARTMENT JOIN HR_EMPLOYEES USING (DEPT_ID)
GROUP BY 1
ORDER BY 3 DESC




