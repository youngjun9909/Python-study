package com.korit.fileupload_back.controller;

import com.korit.fileupload_back.dto.RequestFileUploadDto;
import com.korit.fileupload_back.service.FileUploadService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@RestController
public class FileUploadController {

    @Autowired
    private FileUploadService fileUploadService;

    @CrossOrigin
    @PostMapping("/api/upload")
    public ResponseEntity<?> upload(@ModelAttribute RequestFileUploadDto dto) throws IOException {
        fileUploadService.uploadFile(dto.getImg());
        return ResponseEntity.ok(true);
    }

}
