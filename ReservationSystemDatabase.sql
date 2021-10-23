-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema reservation
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema reservation
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `reservation` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema reservation_system
-- -----------------------------------------------------
USE `reservation` ;

-- -----------------------------------------------------
-- Table `reservation`.`Theatre_Complex`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservation`.`Theatre_Complex` (
  `idTheatre_Complex` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `phone_number` VARCHAR(10) NULL,
  PRIMARY KEY (`idTheatre_Complex`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reservation`.`Theatre`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservation`.`Theatre` (
  `screen_id` INT NOT NULL,
  `max_seats` INT NOT NULL,
  `Theatre_Complex_idTheatre_Complex` INT NOT NULL,
  PRIMARY KEY (`screen_id`, `Theatre_Complex_idTheatre_Complex`),
  INDEX `fk_Theatre_Theatre_Complex_idx` (`Theatre_Complex_idTheatre_Complex` ASC) VISIBLE,
  CONSTRAINT `fk_Theatre_Theatre_Complex`
    FOREIGN KEY (`Theatre_Complex_idTheatre_Complex`)
    REFERENCES `reservation`.`Theatre_Complex` (`idTheatre_Complex`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reservation`.`Movie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservation`.`Movie` (
  `Title` VARCHAR(45) NOT NULL,
  `run_time` TIME NOT NULL,
  `rating` DECIMAL NULL,
  PRIMARY KEY (`Title`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reservation`.`Showing`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservation`.`Showing` (
  `idShowing` INT NOT NULL,
  `start_time` TIME NOT NULL,
  `num_seats` INT NOT NULL,
  `date_played` DATE NOT NULL,
  `Theatre_screen_id` INT NOT NULL,
  `Theatre_Theatre_Complex_idTheatre_Complex` INT NOT NULL,
  `Movie_Title` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idShowing`, `Theatre_screen_id`, `Theatre_Theatre_Complex_idTheatre_Complex`, `Movie_Title`),
  INDEX `fk_Showing_Theatre1_idx` (`Theatre_screen_id` ASC, `Theatre_Theatre_Complex_idTheatre_Complex` ASC) VISIBLE,
  INDEX `fk_Showing_Movie1_idx` (`Movie_Title` ASC) VISIBLE,
  CONSTRAINT `fk_Showing_Theatre1`
    FOREIGN KEY (`Theatre_screen_id` , `Theatre_Theatre_Complex_idTheatre_Complex`)
    REFERENCES `reservation`.`Theatre` (`screen_id` , `Theatre_Complex_idTheatre_Complex`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Showing_Movie1`
    FOREIGN KEY (`Movie_Title`)
    REFERENCES `reservation`.`Movie` (`Title`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reservation`.`User_Account`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservation`.`User_Account` (
  `idUser_Account` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `fname` VARCHAR(45) NOT NULL,
  `lname` VARCHAR(45) NULL,
  `phone_number` VARCHAR(45) NULL,
  `credit_card_number` VARCHAR(20) NULL,
  `credit_card_expiry` VARCHAR(45) NULL,
  PRIMARY KEY (`idUser_Account`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `phone_number_UNIQUE` (`phone_number` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reservation`.`Reservataion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservation`.`Reservataion` (
  `idReservataion` INT NOT NULL,
  `num_tickets` INT NOT NULL,
  `reservataion_time` TIME NULL,
  `fee_payment` TINYINT NOT NULL,
  `Showing_idShowing` INT NOT NULL,
  `Showing_Theatre_screen_id` INT NOT NULL,
  `Showing_Theatre_Theatre_Complex_idTheatre_Complex` INT NOT NULL,
  `Showing_Movie_Title` VARCHAR(45) NOT NULL,
  `User_Account_idUser_Account` INT NOT NULL,
  PRIMARY KEY (`idReservataion`, `Showing_idShowing`, `Showing_Theatre_screen_id`, `Showing_Theatre_Theatre_Complex_idTheatre_Complex`, `Showing_Movie_Title`, `User_Account_idUser_Account`),
  INDEX `fk_Reservataion_Showing1_idx` (`Showing_idShowing` ASC, `Showing_Theatre_screen_id` ASC, `Showing_Theatre_Theatre_Complex_idTheatre_Complex` ASC, `Showing_Movie_Title` ASC) VISIBLE,
  INDEX `fk_Reservataion_User_Account1_idx` (`User_Account_idUser_Account` ASC) VISIBLE,
  CONSTRAINT `fk_Reservataion_Showing1`
    FOREIGN KEY (`Showing_idShowing` , `Showing_Theatre_screen_id` , `Showing_Theatre_Theatre_Complex_idTheatre_Complex` , `Showing_Movie_Title`)
    REFERENCES `reservation`.`Showing` (`idShowing` , `Theatre_screen_id` , `Theatre_Theatre_Complex_idTheatre_Complex` , `Movie_Title`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reservataion_User_Account1`
    FOREIGN KEY (`User_Account_idUser_Account`)
    REFERENCES `reservation`.`User_Account` (`idUser_Account`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reservation`.`User_Account_has_Movie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservation`.`User_Account_has_Movie` (
  `User_Account_idUser_Account` INT NOT NULL,
  `Movie_Title` VARCHAR(45) NOT NULL,
  `Review` VARCHAR(255) NULL,
  PRIMARY KEY (`User_Account_idUser_Account`, `Movie_Title`),
  INDEX `fk_User_Account_has_Movie_Movie1_idx` (`Movie_Title` ASC) VISIBLE,
  INDEX `fk_User_Account_has_Movie_User_Account1_idx` (`User_Account_idUser_Account` ASC) VISIBLE,
  CONSTRAINT `fk_User_Account_has_Movie_User_Account1`
    FOREIGN KEY (`User_Account_idUser_Account`)
    REFERENCES `reservation`.`User_Account` (`idUser_Account`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_Account_has_Movie_Movie1`
    FOREIGN KEY (`Movie_Title`)
    REFERENCES `reservation`.`Movie` (`Title`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
