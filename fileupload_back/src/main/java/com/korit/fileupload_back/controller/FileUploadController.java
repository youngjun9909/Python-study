package com.korit.fileupload_back.controller;

import com.korit.fileupload_back.dto.RequestFileUploadDto;
import com.korit.fileupload_back.service.FileUploadService;
import com.korit.fileupload_back.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@RestController
public class FileUploadController {

    @Autowired
    private MemberService memberService;

    @CrossOrigin
    @PostMapping("/api/upload")
    public ResponseEntity<?> upload(@ModelAttribute RequestFileUploadDto dto) throws IOException {
        return ResponseEntity.ok(memberService.addMember(dto));
    }

}
