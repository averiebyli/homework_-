USE heart_disease;

DROP TABLE IF EXISTS heart_disease_uci;

-- 创建表结构
CREATE TABLE heart_disease_uci (
    id INT,
    age INT,
    sex VARCHAR(10),
    dataset VARCHAR(50),
    cp VARCHAR(50),
    trestbps INT,
    chol INT,
    fbs TINYINT(1),
    restecg VARCHAR(50),
    thalch INT,
    exang TINYINT(1),
    oldpeak FLOAT,
    slope VARCHAR(50),
    ca INT,
    thal VARCHAR(50),
    num INT
);

-- 加载CSV文件数据
LOAD DATA INFILE '/Users/catherine/workspace1/MYSQL_DATA/heart_disease_uci.csv'
INTO TABLE heart_disease_uci
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, age, sex, dataset, cp, @trestbps, @chol, @fbs, restecg, @thalch, @exang, @oldpeak, slope, @ca, thal, num)
SET fbs = CASE WHEN @fbs = 'TRUE' THEN 1 WHEN @fbs = 'FALSE' THEN 0 ELSE NULL END,
    exang = CASE WHEN @exang = 'TRUE' THEN 1 WHEN @exang = 'FALSE' THEN 0 ELSE NULL END,
    ca = CASE WHEN @ca = '' THEN NULL ELSE @ca END,
    chol = CASE WHEN @chol = '' THEN NULL ELSE @chol END,
    trestbps = CASE WHEN @trestbps = '' THEN NULL ELSE @trestbps END,
    thalch = CASE WHEN @thalch = '' THEN NULL ELSE @thalch END,
    oldpeak = CASE WHEN @oldpeak = '' THEN NULL ELSE @oldpeak END;
