# How to USE

example code

```sh
curl --location --request POST 'https://api.ocr.proclubstudio.com/file' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--form 'file=image.jpeg'
```

there are some file with extension of png the first is
320220.png
320227.png
320311.png
```sql
CREATE TABLE `Image` (
	`SeqNum` INT(11) NOT NULL AUTO_INCREMENT,
	`DeviceId` VARCHAR(45) NULL DEFAULT NULL,
	`RefSN` INT(11) NOT NULL,
	`Data` MEDIUMBLOB NULL,
	`Flag` TINYINT(4) NULL DEFAULT '0',
	`ProfileSN` INT(11) NULL DEFAULT NULL,
	PRIMARY KEY (`SeqNum`)

```
```sql
CREATE TABLE `Teks` (
	`SeqNum` INT(11) NOT NULL AUTO_INCREMENT,
	`DeviceId` VARCHAR(45) NULL DEFAULT NULL,
	`RefSN` INT(11) NOT NULL,
	`Data` TEXT NULL,
	`Flag` TINYINT(4) NULL DEFAULT '0',
	`ProfileSN` INT(11) NULL DEFAULT '0',
	`FlagParser` INT(11) NULL DEFAULT '0',
	`FlagClean` INT(11) NULL DEFAULT NULL,
	PRIMARY KEY (`SeqNum`)
)
COMMENT='Menyimpan hasil OCR'
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;

```