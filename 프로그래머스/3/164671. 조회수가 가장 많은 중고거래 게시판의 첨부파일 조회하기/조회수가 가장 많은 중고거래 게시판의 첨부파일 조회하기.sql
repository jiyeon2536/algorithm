# -- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/',B.BOARD_ID, '/', F.FILE) AS FILE_PATH
FROM USED_GOODS_BOARD B
    JOIN (SELECT FILE_ID, BOARD_ID, CONCAT(FILE_ID, FILE_NAME, FILE_EXT) AS FILE
         FROM USED_GOODS_FILE) F 
         ON B.BOARD_ID = F.BOARD_ID
WHERE B.VIEWS = (SELECT MAX(VIEWS) 
                 FROM USED_GOODS_BOARD)
ORDER BY F.FILE_ID DESC
